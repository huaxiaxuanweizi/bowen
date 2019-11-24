# txt = open('a.txt','w',encoding ='utf8')#encoding 编码方式
# txt.write('nihao\n')#\n 是换行
# for a in range(1,10):
#     for b in range(1,a+1):
#         c = a*b
#         txt.write(f'{a}*{b}={c}\t')# \t 指的是 间隔
#
#     txt.write("\n")# 换行

# for a in range(1,101):
#     for b in range(1,5):
#             txt.write('nihao\t')
#     txt.write('\n')

#新的文件 插入内容
# txt = open(r'c:\Users\369\Desktop\abc.txt','w',encoding='utf8')
# txt.write("666")
# for a in range(1,101):
#     for b in range(1,5):
#             txt.write('nihao\t')
#     txt.write('\n')

# #提取内容

# a = open(r'abc.txt''r',encoding='utf8')
# b = a.readlines()

# print(b)
# while True:
#     c = a.readline()
#     print(c)
#     if c==" ":
#         break

# txt = open(r'c:\Users\369\Desktop\abc.txt','r+',encoding='utf8')# r+  是读取
# txt.write("\nabcdefghijklmnopqrstuvwxyz")# \n转行
# print(txt.read())

# a = open(r'c:\Users\369\Desktop\987.jpg','rb')
# b = a.read()
# print(b)
# a.close()
# c = open('a.jpg','wb')
# c.write(b)
# c.close()

# a = open(r'd:\QQMusicCache\MV\云廷公子-绝美翻唱 - 王北车、
# 颜人中等歌手演唱那女孩对我说，你心动了吗(超清).mp4','rb')
# b = a.read()
# print(b)
# a.close()
# c = open('a.mp4','ab')
# c.write(b)
# c.close()
#
# with open('a.txt','r') as f:# as 相当于  =
#     print(f.read())# 执行完 f 后 自动执行close

txt = open(r'c:\users\369\desktop\ccc.txt','w',encoding='utf-8')
for a in range(10):
    for b in range(1,a+1):
        txt.write(f'{a}*{b}={a*b} \t')  # \t 指的是 间隔空
    txt.write('\n')  # 换行

txt = open(r'c:\users\369\desktop\ccc.txt','r+',encoding='utf-8')
a = txt.readlines()
print(a)
