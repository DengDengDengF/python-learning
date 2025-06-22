# 线程启动 -> 主线程执行 -> 线程并发执行 -> 程序结束。
# 与js中的同步异步，有异曲同工之妙。
import threading
import time

exitFlag = 0


class myThread(threading.Thread):  # 继承父类threading.Thread
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):  # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        # 线程启动后执行
        print("Starting " + self.name)
        # 线程并发执行
        print_time(self.name, self.counter, 5)
        # 线程执行完毕
        print("Exiting " + self.name)


def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            (threading.Thread).exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 线程启动，开启主线程
thread1.start()
thread2.start()

# 线程启动后执行
print("Exiting Main Thread")
