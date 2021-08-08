import requests
import pod_class
import pod_list_funcs

def get_data(prometheus_url, query):
  response = requests.get(prometheus_url + '/api/v1/query', params={'query': query})
  results = response.json()['data']['result']
  return results


# Bu ve altındaki fonksiyonları birleştirebiliriz.
def get_requests_from_prometheus(pod_list):
    metrics = get_data('http://prometheus-server:80', 'kube_pod_container_resource_requests')

    for metric in metrics:
        pod_index = pod_list_funcs.get_pod_index(pod_list, metric['metric']['pod'])
        
        if pod_index == -1:
            pod = pod_class.Pod(metric['metric']['pod'])
            pod_list.append(pod)
            pod_index = len(pod_list) - 1

        pod_list[pod_index].set_pod_requests(metric['metric']['resource'], metric['value'][1])


def get_limits_from_prometheus(pod_list):
    metrics = get_data('http://prometheus-server:80', 'kube_pod_container_resource_limits')

    for metric in metrics:
        pod_index = pod_list_funcs.get_pod_index(pod_list, metric['metric']['pod'])
        
        if pod_index == -1:
            pod = pod_class.Pod(metric['metric']['pod'])
            pod_list.append(pod)
            pod_index = len(pod_list) - 1

        pod_list[pod_index].set_pod_limits(metric['metric']['resource'], metric['value'][1])

def get_cpu_usage_from_prometheus(pod_list):
    metrics = get_data('http://prometheus-server:80', 'sum(irate(container_cpu_usage_seconds_total{container!=""}[2m]))by(node,pod)')
    print(metrics)
"""
    for metric in metrics:
        pod_index = pod_list_funcs.get_pod_index(pod_list, metric['metric']['pod'])
        
        if pod_index == -1:
            pod = pod_class.Pod(metric['metric']['pod'])
            pod_list.append(pod)
            pod_index = len(pod_list) - 1

        pod_list[pod_index].set_pod_limits(metric['metric']['resource'], metric['value'][1])
"""