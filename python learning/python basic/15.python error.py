# try:
#     fh = open('test.txt', 'w')
#     fh.write('这是一个测试文件，用于测试异常!!')
# except IOError:
#     # 开启只读后就会执行IOError
#     print('Error:没有找到文件或读取文件失败')
# else:
#     print('没发生异常后执行else,内容写入成功')
#     fh.close()




# try:
#     fh = open('test.txt', 'w')
#     fh.write('这是一个测试文件，用于测试异常!!')
# finally:
#     print('不管是否异常都会执行finally')
#     fh.close()

