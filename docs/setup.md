# Setup

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

Installing GridDyn to work with HELICS:

-   GridDyn’s installation guide can be found at
    <https://github.com/LLNL/GridDyn>

-   Currently only the experimental branch works with HELICS so you will
    need to build that branch of the source code.

Installing Festive Lite:

-   In order to run the Festive Lite example that is part of this
    tutorial you will need to make sure you install the HELICS python
    extension. Please follow the instructions given here
    <https://github.com/GMLC-TDC/HELICS-src/tree/master/python>

Running the Federation:

The TDC Federation example included here consists of 11 GridLAB-D
distribution feeder models each with retail markets that are responding
to a price provided by the wholesale market prices given by Festive AGC
model. The 11 GridLAB-D models are connected to a 5 node Transmission
model in GridDyn. There are 13 federates in total. To run the federation
the first thing to start is a helics\_broker. Open a terminal and type
helics\_broker 13. Then start the other federates. The files to run are
as follows:

GridLAB-D:

1.  HELICS-Tutorial/gldFeeders/B2/DistributionSim\_B2\_G\_1.glm

2.  HELICS-Tutorial/gldFeeders/B2/DistributionSim\_B2\_R\_2\_1.glm

3.  HELICS-Tutorial/gldFeeders/B2/DistributionSim\_B2\_R\_2\_2.glm

4.  HELICS-Tutorial/gldFeeders/B2/DistributionSim\_B2\_R\_2\_2.glm

5.  HELICS-Tutorial/gldFeeders/B3/DistributionSim\_B3\_R\_3\_1.glm

6.  HELICS-Tutorial/gldFeeders/B3/DistributionSim\_B3\_R\_3\_2.glm

7.  HELICS-Tutorial/gldFeeders/B3/DistributionSim\_B3\_R\_3\_3.glm

8.  HELICS-Tutorial/gldFeeders/B3/DistributionSim\_B3\_R\_3\_4.glm

9.  HELICS-Tutorial/gldFeeders/B4/DistributionSim\_B4\_G\_1.glm

10. HELICS-Tutorial/gldFeeders/B4/DistributionSim\_B4\_R\_1\_1.glm

11. HELICS-Tutorial/gldFeeders/B4/DistributionSim\_B4\_R\_1\_2.glm

-   To run each file you simply need to open a terminal at each file
    location and type gridlabd filename.

GridDyn:

1.  HELICS-Tutorial/GridDyn/TDC\_No\_dynamic\_HELICS\_ld\_gen.xml

-   To run the file open a terminal at the file location and run
    griddynMain filename –helics.

Festive Lite:

1.  HELICS-Tutorial/festiv/main.py

-   To run the file open a terminal at the file location and run python
    main.py.
