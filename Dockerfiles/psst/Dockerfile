FROM helics as builder

RUN apt update && apt install -y \
  python3-pip git

RUN pip3 install scipy

WORKDIR /root/develop

RUN git clone https://github.com/kdheepak/psst.git

WORKDIR /root/develop/psst

RUN pip3 install . \
  && cp -a psst/* /usr/local/lib/python3.6/dist-packages/psst

FROM ubuntu:18.04

RUN apt update && apt install -y --no-install-recommends \
  python3-pkg-resources python3-six python3-setuptools python3-idna \
  && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local /usr/local/

ENV LC_ALL=C.UTF-8 LANG=C.UTF-8

CMD ["psst", "--version"]
