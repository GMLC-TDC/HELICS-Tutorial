import time
import helics as h
import random
import logging


helicsversion = h.helicsGetVersion()
print("Federate 1: HELICS version = {}".format(helicsversion))

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


def create_federate(deltat=1.0, fedinitstring="--federates=1"):

    fedinfo = h.helicsCreateFederateInfo()

    status = h.helicsFederateInfoSetCoreName(fedinfo, "Combination Federate")

    h.helicsFederateInfoSetCoreTypeFromString(fedinfo, "zmq")

    status = h.helicsFederateInfoSetCoreInitString(fedinfo, fedinitstring)

    status = h.helicsFederateInfoSetTimeProperty(fedinfo, h.helics_property_time_delta, deltat)

    fed = h.helicsCreateCombinationFederate("Combination Federate", fedinfo)

    return fed

def destroy_federate(fed, broker=None):
    status = h.helicsFederateFinalize(fed)

    status, state = h.helicsFederateGetState(fed)
    assert state == 3

    while (h.helicsBrokerIsConnected(broker)):
        time.sleep(1)

    h.helicsFederateFree(fed)

    h.helicsCloseLibrary()


def main():

    fed = create_federate()

    # Register publication
    pubid = h.helicsFederateRegisterGlobalPublication(fed, "TransmissionSim/B2Voltage", h.helics_data_type_complex, "")
    
    # Register subscription
    subid = h.helicsFederateRegisterSubscription(fed, "DistributionSim_B2_G_1/totalLoad", "")
    
    # Register endpoint
    epid = h.helicsFederateRegisterEndpoint(fed, "ep1", None)

    # Enter execution mode
    h.helicsFederateEnterExecutingMode(fed)

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
            grantedtime = h.helicsFederateRequestTime(fed, t)
        time.sleep(1)
        rValue, iValue = h.helicsInputGetComplex(subid)
        logger.info("Python Federate grantedtime = {}".format(grantedtime))
        logger.info("Load value = {} MVA".format(complex(rValue, iValue)/1000))

    t = 60 * 60 * 24
    while grantedtime < t:
        grantedtime = h.helicsFederateRequestTime (fed, t)
    logger.info("Destroying federate")
    destroy_federate(fed)

if __name__ == "__main__":

    main()
    logger.info("Done!")
