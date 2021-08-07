import datetime
import time
import requests  

PROMETHEUS = 'http://prometheus-server:80'

end_of_month = datetime.datetime.today().replace(day=1).date()

last_day = end_of_month - datetime.timedelta(days=1)
duration = '[' + str(last_day.day) + 'd]'

response =requests.get(PROMETHEUS + '/api/v1/query', params={'query': 'container_cpu_user_seconds_total'})
results = response.json()['data']['result']

print('{:%B %Y}:'.format(last_day))
for result in results:
  print(' {metric}: {value[1]}'.format(**result))