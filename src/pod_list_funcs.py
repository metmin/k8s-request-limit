import config


def get_pod_index(pod_list, pod_name):
    index = 0
    for pod in pod_list:
        if pod.pod_name == pod_name:
            return index
        index = index + 1
    return -1


def calculate_diff(pod_list):
    
    diff_message = ""
    error_message = ""

    for pod in pod_list:

        if pod.cpu_req == "" or pod.mem_req == "" or pod.cpu_usage == "0" or pod.cpu_usage == "":
            # TODO: Slack kanalına ayarlanmadığı ile ilgili mesaj göndersin. - DONE
            # TODO: cpu kullanımı 0'sa da mesaj basabilir. 
            error_message += f"```There is an error about {pod.cluster}/{pod.pod_name} cpu or memory request```\n"
            #_ = slack_api.send_notification("ERROR", config.WEBHOOK_URL, pod)
            continue

        cpu_req   = float(pod.cpu_req)
        cpu_usage = float(pod.cpu_usage)
        mem_req   = int(pod.mem_req)   / 1024 / 1024
        mem_usage = int(pod.mem_usage) / 1024 / 1024
        
        # abs(usage - request) / usage * 100  
        cpu_diff =  abs(cpu_usage - cpu_req) / cpu_usage * 100
        mem_diff =  abs(mem_usage - mem_req) / mem_usage * 100

        if cpu_diff > 10000 or mem_diff > 150:
            #_ = slack_api.send_notification("DIFF", config.WEBHOOK_URL, pod, cpu_diff, mem_diff)
            diff_message += f"```Cluster Name: {pod.cluster}\n\tPod Name: {pod.pod_name}\n\t\tCPU Request: {pod.cpu_req}\n\t\tCPU Usage: {pod.cpu_usage}\n\t\tCPU Diff: %{cpu_diff}\n\t\t--------------------\n\t\tMem Request: {pod.mem_req}\n\t\tMem Usage: {pod.mem_usage}\n\t\tMem Diff: %{mem_diff}```\n"
    

    return diff_message, error_message