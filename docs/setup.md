# Setup

### Install HELICS

See install instructions [here](https://gmlc-tdc.github.io/HELICS-src/installation/index.html).

### Install GridLAB-D

Installing GridLAB-D with HELICS on Linux and MacOS:

-   Make sure GridLAB-D’s prerequisites are installed: automake,
    libtool, xerces-c, gcc, g++, and HELICS of course.

-   Checkout feature branch feature/1024 from the GridLAB-D git
    repository located at <https://github.com/gridlab-d/gridlab-d.git>.

-   On your terminal navigate to your local checkout of the code.

-   Type `autoreconf -if`

-   Then run the following

    ```
    ./configure --prefix=/path/to/gridlabd/install --with-helics=/path/to/helics/install --enable-silent-rules "CFLAGS=-g -O0 -w" "CXXFLAGS=-g -O0 -w -std=c++11" "LDFLAGS=-g -O0 -w"
    ```

-   You need to edit the Makefile that was created by the figure step.
    Find and edit the following lines

    -   Add at the end of line 1049 `–I/path/to/helics/install/include/helics`

    -   If you didn’t install zeromq in the same location as helics you
        will need to edit lines 1050 and 1051. Add to 1050 –L/path/to/zeromq/install/lib/. Add to 1051 `–lzmq`.

-   You are done editing the Makefile. In the terminal type make and
    then make install. You now have successfully built and installed
    GridLAB-D with HELICS.

-   For Sierra users it is important that you compile HELICS and
    GridLAB-D and there prereqs with gcc and not clang. There is an
    outstanding issue with compiling GridLAB-D with Sierra’s version of
    clang.

### Installing GridDyn

Installing GridDyn to work with HELICS:

-   GridDyn’s installation guide can be found at
    <https://github.com/LLNL/GridDyn>

-   Currently only the experimental branch works with HELICS so you will
    need to build that branch of the source code.

### Installing FESTIVLite

Installing FESTIVLite:

-   In order to run the FESTIVLite example that is part of this
    tutorial you will need to make sure you install the HELICS python
    extension. Please follow the instructions given here
    <https://github.com/GMLC-TDC/HELICS-src/tree/master/python>

