# Tutorials

### [Tutorial-1-DistributionFederation-ManualStart](./1-DistributionFederation-ManualStart/README.md)

This is an example of a single GridLAB-D HELICS Federate interacting with a Python HELICS Combination Federate (for logging) and a HELICS Broker.
This example requires starting the federation manually.

### [Tutorial-2-DistributionFederation-HELICSRunner](./2-DistributionFederation-HELICSRunner/README.md)

This is an example of a single GridLAB-D HELICS Federate interacting with a Python HELICS Combination Federate (for logging) and a HELICS Broker.
This example uses `helics_runner` to start the federation.

### [Tutorial-3-TransmissionDistributionFederation-HELICSRunner](./3-TransmissionDistributionFederation-HELICSRunner/README.md)

This is an example of a GridLAB-D HELICS Federates, a GridDyn HELICS Federate and a HELICS Broker.

### [Tutorial-4-TransmissionDistributionMarketsFederation-HELICSRunner](./4-TransmissionDistributionMarketsFederation-HELICSRunner/README.md)

This is an example of 11 GridLAB-D HELICS Federates, a GridDyn HELICS Federate, a FESTIVLite HELICS Federate and a HELICS Broker.

### [Tutorial-5-TransmissionDistributionMarketsCommunicationsFederation-HELICSRunner](./5-TransmissionDistributionMarketsCommunicationsFederation-HELICSRunner/README.md)

This is an example of 11 GridLAB-D HELICS Federates, a GridDyn HELICS Federate, a FESTIVLite HELICS Federate, and a HELICS Broker.
In addition it includes communication delay filter.

### Docker Compose

Each tutorial contains a `docker-compose.yml` file that can be used with
Docker Compose to run the tutorial using Docker containers.

For example:

```
$> cd tutorials/1-DistributionFederation-ManualStart
$> docker-compose up
```

If the relevant Docker images need to be built, Docker Compose will take
care of building them before running the tutorial. If this is the case,
go grab some :coffee: while the images build... it'll be a while.
