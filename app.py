import prometheus_api
import pod_list_funcs
import config

#PROMETHEUS = 'http://prometheus-server:80' #conf dosyasından çekilecek.

# TODO: cluster name (ör: p-checkout-p1-2moon) conf'a eklenecek ileride gitlab pipeline'ından verilecek. Amaç: slack'e mesaj gönderirken kullanılacak. - GitLab ci üzerinden ayarlanması içinçalışılacak.
# TODO: slack entegrasyonu - DONE


pod_list = []

prometheus_api.get_requests_from_prometheus(pod_list, config.PROMETHEUS)
prometheus_api.get_limits_from_prometheus(pod_list, config.PROMETHEUS)
prometheus_api.get_cpu_usage_from_prometheus(pod_list, config.PROMETHEUS)
prometheus_api.get_memory_usage_from_prometheus(pod_list, config.PROMETHEUS)
pod_list_funcs.calculate_cpu_diff(pod_list)


"""
for pod in pod_list:
  print(pod.pod_name)
  print(pod.cpu_req + " => " + pod.cpu_limit + " => " + pod.cpu_usage)
  print(pod.mem_req + " => " + pod.mem_limit + " => " + pod.mem_usage)
  print("-----")
"""


'''
git add . ; git commit -m "upgraded" ; git push
'''

