# Tutorial-1-DistributionFederation-ManualStart

**GridLAB-D + PythonCombinationFederate**

Run in terminal 1

```bash
cd /path/to/HELICS-Tutorial/tutorials/1-DistributionFederation-ManualStart/
helics_broker -f 2 --loglevel=3 --name=mainbroker
```

Run in terminal 2

```bash
cd /path/to/HELICS-Tutorial/tutorials/1-DistributionFederation-ManualStart/
python federate1.py
```

Run in terminal 3

```bash
cd /path/to/HELICS-Tutorial/test_system_data/gldFeeders/B2/G_1/
gridlabd DistributionSim_B2_G_1.glm
```

