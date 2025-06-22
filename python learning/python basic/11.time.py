import time,calendar

ticks = time.time()
print(ticks)

print('当前时间:',time.localtime(time.time()))

cal = calendar.month(2016, 1)
print(cal)