#！/usr/bin/python
#-*-coding:utf8-*-

import time
# 表示是公元 1970年8点开始的到现在所经过的秒数
# second = time.time()

# localtime 本地时间
# shijian = time.localtime()
# print(shijian)
#
# shijian = time.localtime(1000)# 表示是公元 1970年8点开始 后的 1000 秒 是什么时候
# print(shijian)

# # # gmtime  国际化时间
# utc_shijian = time.gmtime()
# print(utc_shijian)

# utc_shijian = time.gmtime(0)#  国际标准化时间 与我们 本地时间相差 8 个小时
# print(utc_shijian)

# tm_wday=0# 表示 周一到 周日  （ 0——6）
# tm_isdst=0 #  夏令时 时间（已经暂停）

# 将结构化时间转化为格式化时间
# geshihua = time.strftime('%Y/%m/%d \n %H:%M:%S',time.localtime())
# print(geshihua)
# geshihua = time.strftime('%Y/%m/%d %X',time.localtime())  # %X = %H:%M:%S
# print(geshihua)

# 将格式化时间转换为结构化时间
# jiegouhua = time.strptime('2019-10-29 00:00:00','%Y-%m-%d %X' )
# print(jiehouhua)
# jiegouhua1 = time.strptime('2019/10/29 09:53:12','%Y/%m/%d %X' )
# print(jiegouhua1)

# 将结构化时间 转化成时间戳
# shijianchuo = time.mktime(time.localtime())
# print(shijianchuo)
# shijianchuo = time.mktime(shijian)
# print(shijianchuo)


# 将结构化时间转化为格式化时间
# 将格式化时间转换为结构化时间
geshihua = time.strftime('%Y/%m/%d %X',time.localtime())  # %X = %H:%M:%S
print(geshihua)
jiegouhua = time.strptime(geshihua,'%Y/%m/%d %X')

# 将格式化时间转换为结构化时间
jiegouhua1 = time.strptime('2019/10/29 09:00:00','%Y/%m/%d %X' )
print(jiegouhua1)
# 将结构化时间转化成时间戳
a = int(time.mktime(jiegouhua)) - int(time.mktime(jiegouhua1))
print(a)

# 程序 开始到最后用的时间
# from time import *# 导入模块
#
# print(localtime())
# print(time())
#
# start = time() # 开始
# for i in range(6):
#     print(i)
#     sleep(3) # 睡眠
#
# end = time() # 结束
# print("这个程序执行时间为%f" % (end - start))