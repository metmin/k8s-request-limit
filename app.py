import requests  

PROMETHEUS = 'http://prometheus-server:80' #conf dosyasından çekilecek.

# TODO: kube_pod_container_resource_requests conf dosyasından çekilecek.
# TODO: cluster name (ör: p-checkout-p1-2moon) conf'a eklenecek ileride gitlab pipeline'ından verilecek. Amaç: slack'e mesaj gönderirken kullanılacak.
# TODO: slack entegrasyonu

class obj:
  def __init__(self, pod, cluster, cpu_req, cpu_limit, cpu_usage, mem_req, mem_limit, mem_usage):
      self.pod = pod
      self.cluster = cluster
      self.cpu_req = cpu_req
      self.cpu_limit = cpu_limit
      self.cpu_usage = cpu_usage
      self.mem_req = mem_req
      self.mem_limit = mem_limit
      self.mem_usage = mem_usage


def get_data(prometheus_url, query):
  response =requests.get(prometheus_url + '/api/v1/query', params={'query': query})
  results = response.json()['data']['result']

  return results

data = get_data('http://prometheus-server:80', 'kube_pod_container_resource_requests')
print(data[0])