FROM helics as builder

RUN apt update && apt install -y \
  libboost-dev libboost-chrono-dev \
  libboost-date-time-dev libboost-filesystem-dev \
  libboost-program-options-dev \
  libboost-test-dev libboost-timer-dev \
  libzmq3-dev libtool libxerces-c-dev \
  build-essential automake git
  

WORKDIR /root/develop

RUN git clone --single-branch -b develop https://github.com/gridlab-d/gridlab-d.git

WORKDIR /root/develop/gridlab-d

RUN autoreconf -if \
  && ./configure --prefix=/usr/local --with-helics=/usr/local --enable-silent-rules \
    "CFLAGS=-g -O0 -w" "CXXFLAGS=-g -O0 -w -std=c++14" "LDFLAGS=-g -O0 -w" \
  && make -j8 install

FROM ubuntu:18.04

RUN apt update && apt install -y --no-install-recommends \
  libboost-chrono1.65.1 libboost-date-time1.65.1 \
  libboost-filesystem1.65.1 libboost-program-options1.65.1 \
  libboost-test1.65.1 libboost-timer1.65.1 \
  libzmq5 libxerces-c3.2 \
  && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local /usr/local/

ENV LD_LIBRARY_PATH=/usr/local/lib

CMD ["gridlabd", "--version"]
