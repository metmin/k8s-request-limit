import os

PROMETHEUS   = []
WEBHOOK_URL  = ""

PROMETHEUS.append(os.environ['THANOS_CHECKOUT_EARTH'])
PROMETHEUS.append(os.environ['THANOS_DELIVERY_EARTH'])
WEBHOOK_URL = os.environ['WEBHOOK_URL']
