# Distribution example


### GridLAB-D + PythonCombinationFederate**

**Option 1**

Run using HELICS Runner

```bash
helics run --path DistributionFederation/config.json
```

**Option 2**

Run manually

Run in terminal 1

```bash
cd /path/to/HELICS-Tutorial/scrpts/distribution-example/DistributionFederation/
python federate1.py > /path/to/HELICS-Tutorial/scripts/distribution-example/DistributionFederation/PythonCombinationFederate.log 2>&1
```

Run in terminal 1

```bash
cd /path/to/HELICS-Tutorial/test_systems/gldFeeders/B2/G_1/
gridlabd DistributionSim_B2_G_1.glm > /path/to/HELICS-Tutorial/scripts/distribution-example/DistributionFederation/GridLABDFederate.log 2>&1
```

See output using the following

```bash
cd /path/to/HELICS-Tutorial/scrpts/distribution-example/DistributionFederation/
tail -f GridLABDFederate.log
```

```bash
cd /path/to/HELICS-Tutorial/scrpts/distribution-example/DistributionFederation/
tail -f PythonCombinationFederate.log
```
