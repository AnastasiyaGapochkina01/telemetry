#!/usr/bin/python3
# pylint: disable=C0103,W,R
import time
import os
import re
import sys
import requests

from prometheus_client import start_http_server, PROCESS_COLLECTOR, PLATFORM_COLLECTOR
from prometheus_client.core import CounterMetricFamily, REGISTRY


class CustomCollector(object):
    def collect(self):
        url = os.environ['TELEMETRY_HOST']
        label = os.environ['LABEL']
        resp = requests.get(url).json()
        for key, value in resp.items():
            key = re.sub('[.]', '_', key)
            c = CounterMetricFamily(str(key), '', labels=[label])
            c.add_metric([key], value)
            yield c


REGISTRY.unregister(REGISTRY._names_to_collectors['python_gc_objects_collected_total'])
REGISTRY.unregister(PLATFORM_COLLECTOR)
REGISTRY.unregister(PROCESS_COLLECTOR)
REGISTRY.register(CustomCollector())


if __name__ == "__main__":
    try:
        LISTEN_PORT = os.environ['PROM_PORT']
    except:
        LISTEN_POST = 8090
    start_http_server(int(LISTEN_PORT))
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nGet keyboard interrupt.Shuting down")
        sys.exit(0)
