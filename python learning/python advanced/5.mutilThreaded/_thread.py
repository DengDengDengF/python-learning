
# 在 Python 中，使用 _thread 模块创建的线程本身是比较底层的，它们不会随着主线程的退出而自动终止

import _thread as thread
import time


# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % (threadName, time.ctime(time.time())), count)


# 创建两个线程
try:
    thread.start_new_thread(print_time, ("Thread-1", 2,))
    thread.start_new_thread(print_time, ("Thread-2", 4,))
except:
    print("Error: unable to start thread")

while 1:
    pass
