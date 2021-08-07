import datetime
import time
import requests  

PROMETHEUS = 'http://prometheus-server:80'

end_of_month = datetime.datetime.today().replace(day=1).date()

last_day = end_of_month - datetime.timedelta(days=1)
duration = '[' + str(last_day.day) + 'd]'

response =requests.get(PROMETHEUS + '/api/v1/query', params={'query': 'kube_pod_container_resource_requests'})
results = response.json()['data']['result']

print('{:%B %Y}:'.format(last_day))
for result in results:
  print(' {metric}: {value[1]}'.format(**result))