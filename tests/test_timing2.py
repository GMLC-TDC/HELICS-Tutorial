import time
import helics as h
import random

def create_value_federate(deltat=1.0, fedinitstring="--federates=1"):

    fedinfo = h.helicsFederateInfoCreate()

    status = h.helicsFederateInfoSetFederateName(fedinfo, "TestB Federate")
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

def destroy_value_federate(fed):
    status = h.helicsFederateFinalize(fed)

    status, state = h.helicsFederateGetState(fed)
    assert state == 3

    h.helicsFederateFree(fed)

    h.helicsCloseLibrary()


def main():

    # print("Creating value federate")
    fed = create_value_federate()

    # print("Registering subscription")
    subid = h.helicsFederateRegisterSubscription (fed, "TransmissionSim/B2Voltage", "complex", "")
    # print("Registering publication")
    pubid = h.helicsFederateRegisterGlobalPublication (fed, "DistributionSim_B2_G_1/totalLoad", "complex", "")

    # print("Setting default value")
    h.helicsSubscriptionSetDefaultComplex(subid, 0, 0)

    # print("Entering execution mode")
    h.helicsFederateEnterExecutionMode(fed)

    hours = 1
    seconds = int(60 * 60 * hours)
    grantedtime = 0
    random.seed(0)
    # for t in range(1, seconds + 1, 60 * 5):
    while grantedtime < 60 * 60 * 24:
        status, receivedRequestedTime, receivedGrantedTime = h.helicsSubscriptionGetComplex(subid)
        print("next requested time by federate = {}".format(receivedRequestedTime))
        print(">>>>>>>> Requesting time = {}".format(60 * 60 * 5))
        time.sleep(2)
        status, grantedtime = h.helicsFederateRequestTime (fed, 60 * 60 * 24)
        print("<<<<<<<< Granted Time = {}".format(grantedtime))
        time.sleep(2)
        status, receivedRequestedTime, receivedGrantedTime = h.helicsSubscriptionGetComplex(subid)
        print("next requested time by federate = {}".format(receivedRequestedTime))
        print("")
        time.sleep(2)

    destroy_value_federate(fed)

if __name__ == "__main__":

    main()




