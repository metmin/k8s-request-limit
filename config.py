import yaml
from yaml.loader import SafeLoader

PROMETHEUS   = []
WEBHOOK_URL  = ""

with open('config.yml') as f:
    config = yaml.load(f, Loader=SafeLoader)

    PROMETHEUS   = config['prometheus_server']
    WEBHOOK_URL  = config['webhook_url']