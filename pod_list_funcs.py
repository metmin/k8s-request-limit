def get_pod_index(pod_list, pod_name):
  index = 0
  for pod in pod_list:
    if pod.pod_name == pod_name:
      # print(pod.pod_name + " => " + pod_name)
      return index
    index = index + 1
    
  return -1


def calculate_cpu_diff(pod_list):
  
  for pod in pod_list:

    if pod.cpu_req == "" or pod.mem_req == "":
      # TODO: Slack kanalına ayarlanmadığı ile ilgili mesaj göndersin.
      continue

    cpu_req   = float(pod.cpu_req) 
    cpu_usage = float(pod.cpu_usage)
    mem_req   = int(pod.mem_req)   / 1024 / 1024
    mem_usage = int(pod.mem_usage) / 1024 / 1024
  
    cpu_diff =  abs(cpu_usage - cpu_req) / cpu_usage * 100    
    mem_diff =  abs(mem_usage - mem_req) / mem_usage * 100    

    # abs(usage - request) / usage * 100 

    print(pod.pod_name)
    print(f"{cpu_req} => {cpu_usage} => {cpu_diff}")
    print(f"{mem_req} => {mem_usage} => {mem_diff}")
    print("-----")

  return 0