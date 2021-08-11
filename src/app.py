import prometheus_api
import pod_list_funcs
import slack_api
import config

# TODO: cluster name (ör: p-checkout-p1-2moon) conf'a eklenecek ileride gitlab pipeline'ından verilecek. Amaç: slack'e mesaj gönderirken kullanılacak. - GitLab ci üzerinden ayarlanması içinçalışılacak.
# TODO: slack entegrasyonu - DONE

pod_list = []

prometheus_url = config.PROMETHEUS


query = prometheus_api.get_ignored_namespaces_query()
prometheus_api.get_requests_from_prometheus(pod_list, prometheus_url, query)
prometheus_api.get_limits_from_prometheus(pod_list, prometheus_url, query)
prometheus_api.get_cpu_usage_from_prometheus(pod_list, prometheus_url, query)
prometheus_api.get_memory_usage_from_prometheus(pod_list, prometheus_url, query)

diff_message, error_message = pod_list_funcs.calculate_diff(pod_list)
_, _ = slack_api.send_notification(config.WEBHOOK_URL, diff_message, error_message)

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

