# socekt网络编程
# netstat -ano | findstr :12345   #查看占用的进程
# taskkill /F /PID 2572          #终止进程
import socket  # 导入 socket 模块

s = socket.socket()  # 创建 socket 对象
host = socket.gethostname()  # 获取本地主机名
port = 12345  # 设置端口
s.bind((host, port))  # 绑定端口


s.listen(5)  # 等待客户端连接

# 死循环，让服务器持续接收。多线程调度。
# js单线程，如果死循环，会占用整个线程导致卡顿。
while True:
    c, addr = s.accept()  # 建立客户端连接
    print('连接地址：', addr)
    c.send('欢迎访问菜鸟教程！'.encode('utf-8'))
    c.close()  # 关闭连接
