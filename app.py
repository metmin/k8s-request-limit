import requests
from requests.api import get  

PROMETHEUS = 'http://prometheus-server:80' #conf dosyasından çekilecek.

# TODO: kube_pod_container_resource_requests conf dosyasından çekilecek.
# TODO: cluster name (ör: p-checkout-p1-2moon) conf'a eklenecek ileride gitlab pipeline'ından verilecek. Amaç: slack'e mesaj gönderirken kullanılacak.
# TODO: slack entegrasyonu

class Pods:
  def __init__(self, pod_name, cluster = 'deneme'):
  #def __init__(self, pod, cluster, cpu_req, cpu_limit, cpu_usage, mem_req, mem_limit, mem_usage):
      self.pod_name = pod_name
      self.cluster = cluster
      '''
      self.cpu_req = cpu_req
      self.cpu_limit = cpu_limit
      self.cpu_usage = cpu_usage
      self.mem_req = mem_req
      self.mem_limit = mem_limit
      self.mem_usage = mem_usage
      '''
  
  # Prometheus sorgularından gelen cevaplar ayrı ayrı listeye kaydedilmesi için farklı fonksiyonlar ayarlandı.
  def set_pod_requests(self, cpu_req, mem_req):
      self.cpu_req = cpu_req
      self.mem_req = mem_req

  def set_pod_limits(self, cpu_limit, mem_limit):
      self.cpu_limit = cpu_limit
      self.mem_limit = mem_limit
  
  def set_pod_cpu_usage(self, cpu_usage):
      self.cpu_usage = cpu_usage
  
  def set_pod_memory_usage(self, mem_usage):
      self.mem_usage = mem_usage

pod_list = []
def get_pod_index(pod_name):
  index = 0
  for pod in pod_list:
    if pod.pod_name == pod_name:
      return index
    index = index + 1
    
  return False



def get_data(prometheus_url, query):
  response =requests.get(prometheus_url + '/api/v1/query', params={'query': query})
  results = response.json()['data']['result']

  return results

metrics = get_data('http://prometheus-server:80', 'kube_pod_container_resource_requests')

for metric in metrics:
  pod = Pods(metric['metric']['pod'])
  pod_index = get_pod_index(pod.pod_name)
  
  if pod_index == False:
    pod_list.append(pod)
    pod_index = len(pod_list) - 1

  if metric['metric']['resource'] == 'cpu':
    pod_list[pod_index].cpu_req = metric['value'][1]
  elif metric['metric']['resource'] == 'memory':
    pod_list[pod_index].mem_req = metric['value'][1]
  #print(metric['metric']['pod'] + " => " + metric['metric']['resource'] + metric['value'][2])


for pod in pod_list:
  print(pod.pod_name)

'''
git add .
git commit -m "upgraded"
git push
'''

