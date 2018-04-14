# Market Transmission Distribution co-simulation example

**Running Federation**

Run using `helics_runner`:

```bash
helics --verbose run --path TransmissionDistributionFederation/config.json
```

`config.json` contains running configurations for

- 11 DistributionSim Federates (GridLABDFederate)
- 1 MarketSim Federate (FESTIVLite)
- 1 TransmissionSim Federate (GridDyn)
