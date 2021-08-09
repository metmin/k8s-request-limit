import yaml
from yaml.loader import SafeLoader

PROMETHEUS   = ""
CLUSTER_NAME = ""
WEBHOOK_URL  = ""

with open('config.yml') as f:
    config = yaml.load(f, Loader=SafeLoader)

    PROMETHEUS   = config['prometheus_server']
    CLUSTER_NAME = config['cluster_name']
    WEBHOOK_URL  = config['webhook_url']