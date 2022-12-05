bind = "127.0.0.1:5000"

workers = 4
# 指定每个工作者的线程数
thread = 2
# 监听内网端口5000

# 工作模式协程
worker_class = 'gevent'
# 设置最大并发量
worker_connections = 2000
