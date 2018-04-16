import sys
import logging
import os
import pandas as pd
import time
import helics as h

current_directory = os.path.realpath(os.path.dirname(__file__))

logger = logging.getLogger('psst.festiv')


def create_federate(deltat=1.0, fedinitstring="--federates=1"):
    logger.debug("Creating federateinfo")
    fedinfo = h.helicsFederateInfoCreate()

    logger.debug("Setting name")
    status = h.helicsFederateInfoSetFederateName(fedinfo, "MarketSim")
    assert status == 0

    logger.debug("Setting core type")
    status = h.helicsFederateInfoSetCoreTypeFromString(fedinfo, "zmq")
    assert status == 0

    logger.debug("Setting init string")
    status = h.helicsFederateInfoSetCoreInitString(fedinfo, fedinitstring)
    assert status == 0

    logger.debug("Setting time delta")
    status = h.helicsFederateInfoSetTimeDelta(fedinfo, deltat)
    assert status == 0

    logger.debug("Setting logging level")
    status = h.helicsFederateInfoSetLoggingLevel(fedinfo, 1)
    assert status == 0

    logger.debug("Creating CombinationFederate")
    fed = h.helicsCreateCombinationFederate(fedinfo)

    return fed

def destroy_federate(fed):
    status = h.helicsFederateFinalize(fed)

    status, state = h.helicsFederateGetState(fed)
    assert state == 3

    h.helicsFederateFree(fed)

    h.helicsCloseLibrary()

def build_DAM_model(day, s):

    mpc = read_festiv(filename)
    mpc.gen['RAMP_10'] = mpc.gen['PMAX']

    for i in range(0, len(s.index)):
        mpc.load.loc[i] = mpc.load.loc[0]

    for b, v in pd.read_excel(filename, sheet_name='LOAD_DIST', index_col=0,).iterrows():
        mpc.load.loc[:, b] = v.values[0] * s.values

    m = build_model(mpc)

    return m


def build_RTM_model(day, load, commitment):

    mpc = read_festiv(filename)
    mpc.gen['RAMP_10'] = mpc.gen['PMAX']

    for b, v in pd.read_excel(filename, sheet_name='LOAD_DIST', index_col=0,).iterrows():
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


def main(delay=None, verbose=False):
    if verbose is not False:
        logger.setLevel(logging.DEBUG)

    logger.info("Creating MockFederate for FESTIV")
    fed = create_federate()

    pubid1 = h.helicsFederateRegisterGlobalTypePublication(fed, "AGCGenDispatch/Alta", h.HELICS_DATA_TYPE_COMPLEX, "")
    pubid2 = h.helicsFederateRegisterGlobalTypePublication(fed, "AGCGenDispatch/Brighton", h.HELICS_DATA_TYPE_COMPLEX, "")
    pubid3 = h.helicsFederateRegisterGlobalTypePublication(fed, "AGCGenDispatch/ParkCity", h.HELICS_DATA_TYPE_COMPLEX, "")
    pubid4 = h.helicsFederateRegisterGlobalTypePublication(fed, "AGCGenDispatch/Solitude", h.HELICS_DATA_TYPE_COMPLEX, "")
    pubid5 = h.helicsFederateRegisterGlobalTypePublication(fed, "AGCGenDispatch/Sundance", h.HELICS_DATA_TYPE_COMPLEX, "")

    h.helicsFederateEnterExecutionMode(fed)

    time_granted = -1
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

        for interval in range(0, int(24 * 60 / 5)):

            for minute in range(0, 5):

                for second in range(0, 60):
                    ticker = ticker + 1

                    if int(second % 6) == 0:
                        stop_at_time = ticker
                        while time_granted < stop_at_time:
                            status, time_granted = h.helicsFederateRequestTime(fed, stop_at_time)
                            logger.info("time granted = {}".format(time_granted))

    destroy_federate(fed)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", action="store_true",
                        help="increase output verbosity")
    parser.add_argument("--delay", type=int,
                        help="delay fixed_price")

    args = parser.parse_args()
    delay = args.delay
    verbose = args.verbose
    main(delay=delay, verbose=verbose)
