import logging
import os
import pandas as pd
import time

from helics import PyValueFederate, PyFederateInfo

from psst.model import build_model

from psst.case import read_festiv

current_directory = os.path.realpath(os.path.dirname(__file__))

filename = os.path.join(current_directory, 'Input', 'PJM_5BUS.xlsx')
timeseries = os.path.join(current_directory, 'Input', 'TIMESERIES')

logger = logging.getLogger('psst.festiv')

logger.setLevel(logging.DEBUG)

N = int(os.environ.get('HELICS_FEDERATES', 13))


def build_DAM_model(day, s):

    mpc = read_festiv(filename)
    mpc.gen['RAMP_10'] = mpc.gen['PMAX']

    for i in range(0, len(s.index)):
        mpc.load.loc[i] = mpc.load.loc[0]

    for b, v in pd.read_excel(filename, sheetname='LOAD_DIST', index_col=0,).iterrows():
        mpc.load.loc[:, b] = v.values[0] * s.values

    m = build_model(mpc)

    return m


def build_RTM_model(day, load, commitment):

    mpc = read_festiv(filename)
    mpc.gen['RAMP_10'] = mpc.gen['PMAX']

    for b, v in pd.read_excel(filename, sheetname='LOAD_DIST', index_col=0,).iterrows():
        mpc.load.loc[:, b] = v.values[0] * load

    for col in mpc.gen['GEN_STATUS'].index:
        mpc.gen_status[col] = 0

    mpc.gen_status = mpc.gen_status.drop('GenCo0', axis=1)

    slice_df = commitment
    mpc.gen_status[slice_df.columns] = slice_df.values

    m = build_model(mpc)

    return m


def get_load(day):
    d = int(day.split('-')[-1]) - 2

    df = pd.read_excel(os.path.join(timeseries, 'ACTUAL_LOAD_DAY_{day}.xlsx'.format(day=d)), index_col=0, parse_dates=True)

    return df


def find_all_topics():

    topics = set()
    for root, _, filenames in os.walk(os.path.abspath(os.path.join(current_directory, './../DummySims/'))):
        for filename in filenames:
            if filename.endswith('.fncsPlayer'):
                with open(os.path.abspath(os.path.join(root, filename))) as f:
                    data = f.read()
                for line in data.splitlines():
                    if line.startswith('#'):
                        continue
                    line = line.replace('\t', ' ')
                    t, topic, value = line.split()
                    topics.add(topic)
    topics = list(topics)

    return topics


def main():

    logger.info("Creating a federate in a `{N}` federate simulation".format(N=N))
    fi = PyFederateInfo(N)
    fi.setName('MarketSim')

    logger.info("Finding all topics")
    topics = find_all_topics()

    logger.info("Creating a ValueFederate")
    vf = PyValueFederate(fi=fi, publications=topics, subscriptions=topics)

    logger.info("Entering executation state")
    vf.enterExecutionState()

    time_granted = 0
    last_second = -1
    ticker = 0

    for day in [
            '2020-08-03',
            '2020-08-04',
            '2020-08-05',
            '2020-08-06',
            '2020-08-07',
            '2020-08-08',
            '2020-08-09',
    ]:

        logger.info("Running DAM for day={day}".format(day=day))
        df = get_load(day)
        dam_s = df.loc[day, 'LOAD'].resample('1H').mean()

        dam_m = build_DAM_model(day, dam_s)
        dam_m.solve('cbc', verbose=False, resolve=True)

        rtm_s = df.loc[day, 'LOAD'].resample('5T').mean()

        for interval in range(0, int(24 * 60 / 5)):
            hour = int(interval * 5 / 60)
            logger.info("Running RTM for day={day} for minute={m} (hour={hour})".format(day=day, m=interval * 5, hour=hour))
            commitment = dam_m.results.unit_commitment.loc[hour:hour, :]
            rtm_m = build_RTM_model(day, rtm_s.iloc[interval], commitment)
            rtm_m.solve('cbc', verbose=False, resolve=True)
            logger.debug("LMP = {lmp} \t Power Generated = {pg}".format(lmp=rtm_m.results.lmp, pg=rtm_m.results.power_generated))

            for minute in range(0, 5):

                for second in range(0, 60):

                    if int(second % 6) == 0:
                        logger.info("Publishing lmp and pg at second = {second} ".format(second=ticker))

                        b2, b3, b4 = rtm_m.results.lmp[['B2', 'B3', 'B4']].values[0]
                        vf.send(str(b2), 'MarketSim/LMP/Bus2')
                        vf.send(str(b3), 'MarketSim/LMP/Bus3')
                        vf.send(str(b4), 'MarketSim/LMP/Bus4')

                        pg = rtm_m.results.power_generated.loc[0].to_dict()

                        vf.send(str(pg['ALTA']), 'MarketSim/AGCGenDispatch/Alta')
                        vf.send(str(pg['BRIGHTON']), 'MarketSim/AGCGenDispatch/Brighton')
                        vf.send(str(pg['PARKCITY']), 'MarketSim/AGCGenDispatch/ParkCity')
                        vf.send(str(pg['SOLITUDE']), 'MarketSim/AGCGenDispatch/Solitude')
                        vf.send(str(pg['SUNDANCE']), 'MarketSim/AGCGenDispatch/Sundance')

                    if ticker != last_second:
                        while time_granted < int(ticker):

                            time_granted = vf.requestTime(int(ticker))
                            #time.sleep(.25)

                        last_second = ticker

                    ticker = ticker + 1


if __name__ == '__main__':
    main()
