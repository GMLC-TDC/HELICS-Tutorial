FROM helics as builder

RUN apt update && apt install -y \
  libboost-dev libboost-chrono-dev \
  libboost-date-time-dev libboost-filesystem-dev \
  libboost-program-options-dev \
  libboost-system-dev libboost-test-dev \
  libboost-timer-dev libsuitesparse-dev \
  libzmq3-dev libklu1 \
  build-essential cmake git

WORKDIR /root/develop

RUN git clone --single-branch -b cmake_update https://github.com/LLNL/GridDyn.git

WORKDIR /root/develop/GridDyn

ADD fmi-patch.diff .
RUN git apply fmi-patch.diff

WORKDIR /root/develop/GridDyn/build

RUN cmake -DHELICS_EXECUTABLE=ON .. && make -j8 install

FROM ubuntu:18.04

RUN apt update && apt install -y --no-install-recommends \
  libboost-chrono1.65.1 libboost-date-time1.65.1 \
  libboost-filesystem1.65.1 libboost-program-options1.65.1 \
  libboost-system1.65.1 libboost-test1.65.1 \
  libboost-timer1.65.1 libzmq5 libklu1 libgomp1 \
  && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local /usr/local/

# FIXME
CMD ["gridDynMain", "--version"]
