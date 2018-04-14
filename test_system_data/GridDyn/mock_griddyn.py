import time
import helics as h
import random
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)


def create_federate(deltat=1.0, fedinitstring="--federates=1"):

    fedinfo = h.helicsFederateInfoCreate()

    status = h.helicsFederateInfoSetFederateName(fedinfo, "Mock GridDyn")
    assert status == 0

    status = h.helicsFederateInfoSetCoreTypeFromString(fedinfo, "zmq")
    assert status == 0

    status = h.helicsFederateInfoSetCoreInitString(fedinfo, fedinitstring)
    assert status == 0

    status = h.helicsFederateInfoSetTimeDelta(fedinfo, deltat)
    assert status == 0

    status = h.helicsFederateInfoSetLoggingLevel(fedinfo, 1)
    assert status == 0

    fed = h.helicsCreateCombinationFederate(fedinfo)

    return fed

def destroy_federate(fed):
    status = h.helicsFederateFinalize(fed)

    status, state = h.helicsFederateGetState(fed)
    assert state == 3

    h.helicsFederateFree(fed)

    h.helicsCloseLibrary()


def main():

    fed = create_federate()

    pubid1 = h.helicsFederateRegisterGlobalTypePublication (fed, "GenOutput/Alta", h.HELICS_DATA_TYPE_COMPLEX, "")
    pubid2 = h.helicsFederateRegisterGlobalTypePublication (fed, "GenOutput/Brighton", h.HELICS_DATA_TYPE_COMPLEX, "")
    pubid3 = h.helicsFederateRegisterGlobalTypePublication (fed, "GenOutput/ParkCity", h.HELICS_DATA_TYPE_COMPLEX, "")
    pubid4 = h.helicsFederateRegisterGlobalTypePublication (fed, "GenOutput/Solitude", h.HELICS_DATA_TYPE_COMPLEX, "")
    pubid5 = h.helicsFederateRegisterGlobalTypePublication (fed, "GenOutput/Sundance", h.HELICS_DATA_TYPE_COMPLEX, "")

    subid1 = h.helicsFederateRegisterSubscription(fed, "DistributionSim_B4_G_1/totalLoad", "complex", "")
    subid2 = h.helicsFederateRegisterSubscription(fed, "DistributionSim_B4_R_1_2/totalLoad", "complex", "")
    subid3 = h.helicsFederateRegisterSubscription(fed, "DistributionSim_B4_R_1_1/totalLoad", "complex", "")
    subid4 = h.helicsFederateRegisterSubscription(fed, "DistributionSim_B3_R_3_4/totalLoad", "complex", "")
    subid5 = h.helicsFederateRegisterSubscription(fed, "DistributionSim_B3_R_3_3/totalLoad", "complex", "")
    subid6 = h.helicsFederateRegisterSubscription(fed, "DistributionSim_B3_R_3_2/totalLoad", "complex", "")
    subid7 = h.helicsFederateRegisterSubscription(fed, "DistributionSim_B3_R_3_1/totalLoad", "complex", "")
    subid8 = h.helicsFederateRegisterSubscription(fed, "DistributionSim_B2_G_1/totalLoad", "complex", "")
    subid9 = h.helicsFederateRegisterSubscription(fed, "DistributionSim_B2_R_2_3/totalLoad", "complex", "")
    subid10 = h.helicsFederateRegisterSubscription(fed, "DistributionSim_B2_R_2_2/totalLoad", "complex", "")
    subid11 = h.helicsFederateRegisterSubscription(fed, "DistributionSim_B2_R_2_1/totalLoad", "complex", "")

    subid12 = h.helicsFederateRegisterSubscription(fed, "MarketSim/AGCGenDispatch/Alta", "double", "")
    subid13 = h.helicsFederateRegisterSubscription(fed, "MarketSim/AGCGenDispatch/Brighton", "double", "")
    subid14 = h.helicsFederateRegisterSubscription(fed, "MarketSim/AGCGenDispatch/ParkCity", "double", "")
    subid15 = h.helicsFederateRegisterSubscription(fed, "MarketSim/AGCGenDispatch/Solitude", "double", "")
    subid16 = h.helicsFederateRegisterSubscription(fed, "MarketSim/AGCGenDispatch/Sundance", "double", "")

    h.helicsFederateEnterExecutionMode(fed)

    hours = 1
    seconds = int(60 * 60 * hours)
    grantedtime = -1
    random.seed(0)
    for t in range(0, seconds, 60 * 5):
        status, value = h.helicsSubscriptionGetDouble(subid12)
        c = complex(value, 0)
        status = h.helicsPublicationPublishComplex(pubid1, c.real, c.imag)
        status, value = h.helicsSubscriptionGetDouble(subid13)
        c = complex(value, 0)
        status = h.helicsPublicationPublishComplex(pubid2, c.real, c.imag)
        status, value = h.helicsSubscriptionGetDouble(subid14)
        c = complex(value, 0)
        status = h.helicsPublicationPublishComplex(pubid3, c.real, c.imag)
        status, value = h.helicsSubscriptionGetDouble(subid15)
        c = complex(value, 0)
        status = h.helicsPublicationPublishComplex(pubid4, c.real, c.imag)
        status, value = h.helicsSubscriptionGetDouble(subid16)
        c = complex(value, 0)
        status = h.helicsPublicationPublishComplex(pubid5, c.real, c.imag)
        # status = h.helicsEndpointSendEventRaw(epid, "fixed_price", 10, t)
        while grantedtime < t:
            status, grantedtime = h.helicsFederateRequestTime (fed, t)
        time.sleep(1)
        logger.info("Python Federate grantedtime = {}".format(grantedtime))

    t = 60 * 60 * 24
    while grantedtime < t:
        status, grantedtime = h.helicsFederateRequestTime (fed, t)
    logger.info("Destroying federate")
    destroy_federate(fed)


if __name__ == "__main__":

    main()
    logger.info("Done!")





