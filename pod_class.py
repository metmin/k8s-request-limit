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