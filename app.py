import requests  

PROMETHEUS = 'http://prometheus-server:80' #conf dosyasından çekilecek.


def get_data(prometheus_url, query):
  response =requests.get(prometheus_url + '/api/v1/query', params={'query': query})
  results = response.json()['data']['result']

  return results

print(get_data('http://prometheus-server:80', 'kube_pod_container_resource_requests'))