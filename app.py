import prometheus_api
import pod_class

PROMETHEUS = 'http://prometheus-server:80' #conf dosyasından çekilecek.

# TODO: kube_pod_container_resource_requests conf dosyasından çekilecek.
# TODO: cluster name (ör: p-checkout-p1-2moon) conf'a eklenecek ileride gitlab pipeline'ından verilecek. Amaç: slack'e mesaj gönderirken kullanılacak.
# TODO: slack entegrasyonu


pod_list = []

def get_pod_index(pod_name):
  index = 0
  for pod in pod_list:
    if pod.pod_name == pod_name:
      # print(pod.pod_name + " => " + pod_name)
      return index
    index = index + 1
    
  return -1



metrics = prometheus_api.get_data('http://prometheus-server:80', 'kube_pod_container_resource_requests')


for metric in metrics:

  pod = pod_class.Pods(metric['metric']['pod'])
  pod_index = get_pod_index(pod.pod_name)
  
  if pod_index == -1:
    pod_list.append(pod)
    pod_index = len(pod_list) - 1

  if metric['metric']['resource'] == 'cpu':
    pod_list[pod_index].cpu_req = metric['value'][1]
  elif metric['metric']['resource'] == 'memory':
    pod_list[pod_index].mem_req = metric['value'][1]


for pod in pod_list:
  print(pod.pod_name)
  print(pod.cpu_req)
  print("-----")

'''
git add .
git commit -m "upgraded"
git push
'''

