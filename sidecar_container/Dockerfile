FROM ubuntu:20.04

RUN apt-get update \
    && apt-get install -y --no-install-recommends python3-pip curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY image/requirements.txt /tmp/requirements.txt

RUN pip3 install --no-cache-dir --ignore-installed -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

ENV PROM_PORT=8090
COPY image/bin/telemetry_prometheus.py /usr/bin

RUN chmod +x /usr/bin/telemetry_prometheus.py

# hadolint ignore=DL3025
CMD /usr/bin/telemetry_prometheus.py
