def get_pod_index(pod_list, pod_name):
  index = 0
  for pod in pod_list:
    if pod.pod_name == pod_name:
      # print(pod.pod_name + " => " + pod_name)
      return index
    index = index + 1
    
  return -1