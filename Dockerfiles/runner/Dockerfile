FROM helics as builder

RUN apt update && apt install -y \
  python3-pip git

RUN pip3 install git+git://github.com/GMLC-TDC/helics-runner.git@master

FROM ubuntu:18.04

RUN apt update && apt install -y --no-install-recommends \
  python3-pkg-resources python3-six \
  && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr/local /usr/local/

ENV LC_ALL=C.UTF-8 LANG=C.UTF-8

# The config file defaults to calling `python`.
RUN ln -s /usr/bin/python3 /usr/bin/python

CMD ["helics", "--version"]
