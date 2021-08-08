import requests
import pod_class
import pod_funcs

def get_data(prometheus_url, query):
  response = requests.get(prometheus_url + '/api/v1/query', params={'query': query})
  results = response.json()['data']['result']

  return results


def set_pod_requests(pod_list):
    metrics = get_data('http://prometheus-server:80', 'kube_pod_container_resource_requests')

    for metric in metrics:
        pod = pod_class.Pods(metric['metric']['pod'])
        pod_index = pod_funcs.get_pod_index(pod.pod_name)
        
        if pod_index == -1:
            pod_list.append(pod)
            pod_index = len(pod_list) - 1

        if metric['metric']['resource'] == 'cpu':
            pod_list[pod_index].cpu_req = metric['value'][1]
        elif metric['metric']['resource'] == 'memory':
            pod_list[pod_index].mem_req = metric['value'][1]
