bind = "127.0.0.1:5000"

workers = 4
# 指定每个工作者的线程数
thread = 2
# 监听内网端口5000

# 工作模式协程
worker_class = 'gevent'
# 设置最大并发量
worker_connections = 2000
# 设置访问日志和错误信息日志路径
ccesslog = './log/gunicorn_acess.log'
errorlog = './log/gunicorn_error.log'
#设置这个值为true 才会把打印信息记录到错误日志里
capture_output = True
# 设置日志记录水平
