import time
import helics as h
import random
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

def create_broker():
    initstring = "2 --name=mainbroker"
    broker = h.helicsCreateBroker("zmq", "", initstring)
    isconnected = h.helicsBrokerIsConnected(broker)

    if isconnected == 1:
        pass

    return broker


def create_value_federate(broker, deltat=1.0, fedinitstring="--broker=mainbroker --federates=1"):

    fedinfo = h.helicsFederateInfoCreate()

    status = h.helicsFederateInfoSetFederateName(fedinfo, "TestA Federate")
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

def destroy_value_federate(fed, broker):
    status = h.helicsFederateFinalize(fed)

    status, state = h.helicsFederateGetState(fed)
    assert state == 3

    while (h.helicsBrokerIsConnected(broker)):
        time.sleep(1)

    h.helicsFederateFree(fed)

    h.helicsCloseLibrary()


def main():

    broker = create_broker()
    fed = create_value_federate(broker)

    pubid = h.helicsFederateRegisterGlobalTypePublication (fed, "TransmissionSim/B2Voltage", h.HELICS_DATA_TYPE_COMPLEX, "")
    subid = h.helicsFederateRegisterSubscription (fed, "DistributionSim_B2_G_1/totalLoad", "complex", "")
    epid = h.helicsFederateRegisterEndpoint(fed, "ep1", None)

    h.helicsSubscriptionSetDefaultComplex(subid, 0, 0)

    h.helicsFederateEnterExecutionMode(fed)

    hours = 1
    seconds = int(60 * 60 * hours)
    grantedtime = -1
    random.seed(0)
    for t in range(0, seconds, 60 * 5):
        c = complex(132790.562, 0) * (1 + (random.random() - 0.5)/2)
        logger.info("Voltage value = {} kV".format(abs(c)/1000))
        status = h.helicsPublicationPublishComplex(pubid, c.real, c.imag)
        # status = h.helicsEndpointSendEventRaw(epid, "fixed_price", 10, t)
        while grantedtime < t:
            status, grantedtime = h.helicsFederateRequestTime (fed, t)
        time.sleep(1)
        status, rValue, iValue = h.helicsSubscriptionGetComplex(subid)
        logger.info("Python Federate grantedtime = {}".format(grantedtime))
        logger.info("Load value = {} MW".format(complex(rValue, iValue)/1000))

    t = 60 * 60 * 24
    while grantedtime < t:
        status, grantedtime = h.helicsFederateRequestTime (fed, t)
    logger.info("Destroying federate")
    destroy_value_federate(fed, broker)


if __name__ == "__main__":

    main()
    logger.info("Done!")




