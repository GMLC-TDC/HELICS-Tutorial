# Setup

### Install HELICS

See install instructions [here](https://helics.readthedocs.io/en/latest/installation/index.html).

### Install HELICSRunner

See install instructions [here](https://github.com/GMLC-TDC/helics-runner).

### Install GridLAB-D

Installing GridLAB-D with HELICS on Linux and MacOS:

-   Make sure GridLAB-D’s prerequisites are installed: automake,
    libtool, xerces-c, gcc, g++, and HELICS of course.
-   Checkout the `develop` branch from the GridLAB-D git
    repository located at <https://github.com/gridlab-d/gridlab-d.git>.
-   On your terminal navigate to your local checkout of the code.
-   Type `autoreconf -if`
-   Then run the following
    ```
    ./configure --prefix=/path/to/gridlabd/install --with-helics=/path/to/helics/install --enable-silent-rules "CFLAGS=-g -O0 -w" "CXXFLAGS=-g -O0 -w -std=c++14" "LDFLAGS=-g -O0 -w"
    ```
-   For Sierra users it is important that you compile HELICS and
    GridLAB-D and there prereqs with gcc and not clang. There is an
    outstanding issue with compiling GridLAB-D with Sierra’s version of
    clang.
    ```
    ./configure --prefix=/path/to/gridlabd-cc/install/ --with-helics=/path/to/helics/install/ --enable-silent-rules CC='gcc-7' CXX='g++-7' CFLAGS='-g -O0 -w' CXXFLAGS='-g -O0 -w -std=c++14' LDFLAGS='-g -O0 -w'
    ```

### Installing GridDyn

Installing GridDyn to work with HELICS:

-   GridDyn’s installation guide can be found at
    <https://github.com/LLNL/GridDyn>
-   Currently only the `cmake_update` branch works with HELICS so you will
    need to build that branch of the source code.

### Installing FESTIVLite

Installing FESTIVLite:

-   In order to run the FESTIVLite example that is part of this
    tutorial you will need to make sure you install the HELICS python
    extension.
-   Install `psst` from [here](https://github.com/kdheepak/psst).
-   Make sure you have the latest version of HELICS built with the Python extension enabled. Please follow the instructions in the [installation page](https://helics.readthedocs.io/en/latest/installation/language.html#helics-with-python3) for more information.

