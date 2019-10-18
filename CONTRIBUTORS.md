# Contributors
This file describes the contributors to the HELICS library and the software used as part of this project
If you would like to contribute to the HELICS project see [CONTRIBUTING](CONTRIBUTING.md)
## Individual contributors
### Pacific Northwest National Lab
-   Andy Fisher*

### Lawrence Livermore National Lab
-   Ryan Mast*
-   Philip Top*

### National Renewable Energy Lab
-   Dheepak Krishnamurthy*

### Other
[Cody Rooks](https://github.com/rookscody) University of Tennessee (Knoxville)

## Used Libraries or Code
### [HELICS](https://github.com/GMLC-TDC/HELICS)  
Most of the original code for this library was pulled from use inside HELICS. Several examples were initially included in the HELICS repo but were pulled out when this repo was created  HELICS is released with a BSD-3-Clause license.

### [GridDyn](https://github.com/LLNL/GridDyn)
GridDyn supports HELICS in experimental versions, and several components of GridDyn code were used in the development of HELICS, given they have several of the same authors.  

### [GridLAB-D](https://www.gridlabd.org/), an open-source tool for distribution power-flow, DER models, basic house thermal and end-use load models, and more. HELICS support currently (8/15/2018) provided in the [`develop` branch](https://github.com/gridlab-d/gridlab-d/tree/develop) which you have to build yourself as described [here](https://github.com/GMLC-TDC/HELICS-Tutorial/tree/master/setup).

### [FestivLite](https://www.nrel.gov/grid/festiv-model.html) NREL's Flexible Energy Scheduling Tool for Integrating Variable Generation (FESTIV) simulates the behavior of the electric power system to help researchers understand the impacts of variability and uncertainty on power system operations.