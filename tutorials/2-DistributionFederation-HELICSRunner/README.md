# Tutorial-2-DistributionFederation-HELICSRunner

**GridLAB-D + PythonCombinationFederate**

The `helics-cli run` does not respect the `broker: true` flag. This is a known issue, and a fix is currently being implemented. 

Because of this, to run this example you need to create the broker manually. Once this issue is fixed, getting this example running will only require the commands in terminal 2. 

### Create Broker Manually

Run in terminal 1 

```bash
cd /path/to/HELICS-Tutorial/tutorials/2-DistributionFederation-HELICSRunner/
helics_broker -f 2 --loglevel=3 --name=mainbroker
```

### Run the co-simulation

Run in terminal 2

```bash
cd /path/to/HELICS-Tutorial/tutorials/2-DistributionFederation-ManualStart/
helics run --path config.json
```

### Monitor outputs (optional)

Run in terminal 3

```bash
cd /path/to/HELICS-Tutorial/tutorials/2-DistributionFederation-ManualStart/
tail -f ./PythonCombinationFederate.log
```

Run in terminal 4

```bash
cd /path/to/HELICS-Tutorial/tutorials/2-DistributionFederation-ManualStart/
tail -f ./GridLABDFederate.log
```


