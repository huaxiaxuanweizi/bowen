# import random# 随机数据库
# while True:
#     a = int(input("请猜拳：1 = 石头 , 2 = 剪刀 , 3 = 布:"))
#     b = random.randint(1,3)
#     print("电脑出的是：（1 = 石头 , 2 = 剪刀 , 3 = 布) %d" %b)
#     if (a==1 and b==2) or (a==2 and b==3) or (a==3 and b==1):
#         print("玩家赢")
#     elif a == b:
#         print("平局")
#     else:
#         print("电脑赢")

#求100以内的质数
# a = 2
# c = 0
# while a <= 100:#100以内
#     b = 2#b限制从2开始
#     while a > b : #如果 a 除以 b 余数等于 0 的话 a 就 加 1 ，如果 a 除以 b 余数不等于 0 就累计
#         if a % b == 0: #如果a 除以 b 余数等于 0
#             break  #退出到 a += 1
#         b = b + 1  #如果 a 除以 b 余数不等于0 就一直加 1 ，看 a 除以 a 内的数有没有等于0 的
#     else: #a 除以  b（a 内的数） 余数没有等于0 的 就累计
#         c = c + a
#     a = a + 1
# print(c)

# c = 0
# for a in range(2,101):# for 会自动循环，不需要再去加1，会循环 2——100，最后一个数 101，不会循环
#     for b in range(2,a):#每次都是从2开始循环，到 a  后就不会循环了
#         if a % b == 0:
#             break # 跳出循环，到 a 重新获取a值
#     else:
#             c = c + a
# print(c)

#九九乘法表
# a = 0
# while a <= 9:
#     b = 1
#     while  b <= a:
#         print("%d*%d=%d"%(b,a,a*b) , end="\t") #end="\t" 指的是 不分行 ，\t指的是 间距一样
#         b = b + 1
#     print("")# 当 b>a 时空格，执行下一条
#     a = a+1 #a 一直加 1 直到 大于 9，就退出

# for a in range(1,10):
#     for b in range(1,a+1):
#         print("%d*%d=%d"%(b,a,a*b),end="\t")
#     print("")

# 随机用 1、2、3、4 组合3位数，不重复
# a = 1
# while a < 5:
#     b = 1
#     while b < 5:
#         c = 1
#         while c < 5:
#             if a != b and b !=c and c != a:
#                 print("%d%d%d" % (a, b, c),end="\t")
#             c = c + 1
#         b = b + 1
#     a = a + 1

# for a in range(1,5):
#    for b in range(1,5):
#         for c in range (1,5):
#             if a != b and b !=c and c !=a:
#                 print("%d%d%d" % (a,b,c),end=" ")

#  #水仙花数
# a = 100
# while a < 1000:
#     b = a // 100
#     c = (a - b*100)  // 10
#     d = a - b*100-c*10
#     if (b**3 + c**3+ d**3 == a ):
#         print(a,end="\t")
#     a = a + 1

# for a in range(100,1000):
#     b = a // 100
#     c = (a - b*100) // 10
#     d = (a - b*100) % 10
#     if (b**3 + c**3+ d**3 == a ):
#      print(a,end="\t")

#算出来：1-2+3-4+5-6+7.....+99
# c = 0
# d = 0
# for a in range(1,100,2):
#     c = c + a
# for b in range(2,99,2):
#     d = b + d
# print("%d" % (c - d) )

# #排序
# a = [85,95,34,65,84,56]
# b = a[:]
# b.sort(reverse=True)
# print(b)
# #冒泡排序
# a = [85,95,34,65,84,56]
# for i in range(len(a)-1):# 循环a - 1 次
#     for j in range(len(a)-1):# 排序 0 到 a-1次
#         if a[j] < a[j+1]:#比较 排序
#             a[j],a[j+1] = a[j+1],a[j]
# print(a)

# a = [2,33,5,6,9,1,58,99,756,952,954,555]
# for b in range(len(a)-1):#循环11 次
#     for c in range(len(a)-1):#循环 11 次
#         if a[c]>a[c+1]:
#             a[c],a[c+1] = a[c+1],a[c]
# print(a)

# #选择法排序
# a = [85,95,34,65,84,56]
# for b in range(len(a)-1):# 排序a - 1 次
#     for c in range(b+1,len(a)):
#         if a[b] > a[c]:
#             a[b],a[c]=a[c],a[b]
#             print(a)

#     for c in range(len(a)-1):
#     for c in range(b+1,len(a)):
# a = [85,95,34,65,84,56]

#.sort 排序
# b = a[:]
# b.sort(reverse=True)
# print(b)

# for a in range(1,10):
#     for b in range(1,10):
#         if a>=b:
#             c = '{}*{}={}'.format(b,a,a*b)
#             print(c,end="\t")
#     print("")

# 1. 将首字母 a与 A 尾字母 c的打印出来：
# a = ['abc','ABc','add','cda']
# for b in a:
#     if (b[0] == 'a' or b[0] == 'A') and b[-1] =='c':
#         print(b)

# a = ['abc','ABc','add','cda']
# for x in a:
#     if x.startswith('a') or  x.startswith('A'):
#         if x.endswith('c'):
#             print(x)
#2 手动输入一个字符串，将字符串的首字母变大写、如果含有字母a，把 a 替换成 123、有空格就删除
# while True:
#     a = input("请输入字符串：")
#     a = a.replace(' ','')
#     a = a.title()
#     a = a.replace('a','123')
#     print(a)
# 3 去除列表中重复的数据
# a = [12,12,12,234,123,1324,12,12,234]
# for b in a: # b 在a里
#     if a.count(b) > 1:#统计a中有几个b,如果统计b中的数据c 大于1的话
#         for z in range(a.count(b)-1):# a统计出来b的数量减去1 ， 剩余的数量就是 z ，进行for循环
#             a.remove(b)#删除a 中的b
# print(a)#最后把a打印出来

# b = [12,234,123,1324,12,12,234]
# c = []
# for a in b:
#     if a not in c:#如果a不在c里面
#         c.append(a)#把a 追加到 c里面
# print(c)

# 4 猜数字，只有三次机会，同一个数字
# import random
# a = random.randint(0, 10)
# c = 0
# d = 3
# while c < 3:
#     c = c+1
#     d = d-1
#     b = int(input("请输入你猜的数字："))
#     if a > b:
#         print("猜的比实际小,还有%s次机会"%d)
#     elif a == b:
#         print("恭喜")
#         break
#     elif a < b:
#         print("猜的比实际大,还有%s次机会"%d)
# else:
#     print("zhazha")

# a = ['手机','电脑','鼠标垫','游艇']
# for c,d in enumerate(a):
#     print(c,d)
# b = int(input("请输入您需要的商品号： "))
# print(a[b])

#1 将 大于66的保存到第一个值中，将 小于66 的保存到第二个值中
# a = [11,22,33,44,55,66,77,88,99,90]
# z = {'大于66':[],'小于66':[]}#将键定义后，值为一个 列表，再插入
# for b in a:
#     if b > 66:
#         z['大于66'].append(b)
#     elif b < 66:
#         z['小于66'].append(b)
# print(z)

#2 查找列表中的元素，移除每个元素的空格，并查找 以 a或A开头并且以c 结尾的所有元素
# dic = {'k1':"al e  x",'k2':"ar  ic",'k3':"Al   ec  ","k4":"T  ony"}.values()
# z = {'xinde':[]}
# for a in dic:
#     a = a.replace(' ', '')
#     if a.startswith('a') or a.startswith('A'):
#         if a.endswith('c'):
#             z['xinde'].append(a)
# print(z)

# 把英文和字母 分离出来
# l = [1,2,4,3,99,66,55,'a','b','c']
# a = []
# b = []
# for i in l:
#     if type(i) == int:
#         a.append(i)
#     elif type(i) == str:
#         b.append(i)
# print(a)
# print(b)

# 因数之和
# for b in range(2,101):
#     a = 0
#     for c in range(1,b):
#         if b%c == 0: #如果 b 除以 c  余数 等于0 的话，c 就添加到 a
#             a = c + a# 把 因数 相加起来
#     if a == b:#如果 a = b ，就打印a      b指的是循环的数
#         print(a)

# #1  找出下面列表中，名字中字母‘e’出现的次数大于等于2次的名字。
# names=[['Tom','Billy','Jefferson','Andrew','Wesley','Steven','Joe'],
#     ['Alice','Jill','Ana','Wendy','Jennifer','Sherrye','Eva']]
# for name in names:
#     for a in name:
#         if a.count("e")>=2:
#             print(a)

# #2   颠倒字典的键名和值
# z = {'a': 10, 'b': 34}
# for y,x in z.items():
#     print({x,y},end="\t")
# h = {x:y for y ,x in z.items()}# 或者这个方法
# print(h)

#3  随机输入一个纯字母的字符，把字符中的字母按出现次数 从高到底进行排序
# a = input("请输入一串字符：")
# b = list(set(a)) # 把a的类型定义成 集合（集合：无序的、不重复的）和 列表类型 成为 b
# c = []
# for d in b:# b现在是 不重复的一个列表，从b中取d
#     e = str(a.count(d))# 统计出来 a中有几个d （ e 是数字 ），注意 把a定义成字符串形式统计
#     c.append(d + e)#把数字与字母相加 ，成为新的字符串
#     c.sort(reverse=True)#排序
# print(c)
# for f in c:# f 是 c列表 里 的值
#     print(f[-1],end="\t") #把列表的第一个数字的 最后一位取出来 例：400c   c 为最后一个

# 4 列表推导式
# a =0
# for i in range(2,101):
#     b = [j for j in range(2,i) if i%j == 0]
#     if len(b) == 0:
#         a = a+i
# print(a)

#5  a 中集合的和如果等于b的话，就打印出来
# a = [1,8,4,56,6,7,89,523,5] #a 是列表
# b = 12 #是整数
# for c in range(len(a)-1): #c 是 循环  第一次取1 和下面的 d 依次相加
#     for d in range(c + 1,len(a)): # d 是 循环 第一次取 8，第二次 取4 ，第三次取 56 以此类推
#         if a[c] + a[d]==b: # 如果c 加 d 等于 b 就打印
#             print(a[c],a[d])

# def dy(a,b):
#     for i in range(len(a)):
#         for j in range((i+1),len(a)):
#             if a[i] + a[j] ==b:
#                 print(a[i],a[j])
# dy([111,2222,3333,4444,222],333)

#  将二进制转换成十进制
# a = input("请输入一个二进制：")
# b = a[::-1]
# c = 0
# for i in range(len(a)):
#     d = int(b[i])*2**i
#     c = c+d
# print(c)

#将一个十进制转换成二进制
# a = int(input("请输入一个十进制："))
# z = list( )
# while True:
#     c,d = divmod(a,2)
#     z.append(d)
#     a  =  c
#     if a ==0 :
#         break
# list(reversed(z))
# for n in z:
#     print(n,end="\t")
# print("")

# a = bin(99)
# print(a)#0b 指2进制

#19.	用100元买100只鸡，公鸡2元一只，母鸡1元一只，小鸡0.5元一只
# # 问买公鸡、母鸡、小鸡各几只
# a = 2
# b = 1
# c = 0.5
# z = 100
# for d in range(100):
#     for e in range(100):
#         for f in range(100):
#             if 2 * d + e + 0.5 * f == z:
#                 if d + e + f ==z:
#                     print(d,e,f)
# 1 九九乘法表
# for a in range(1,10):
#     for b in range(1,10):
#         if b <= a:
#             print("%d*%d=%d"%(b,a,a*b),end="\t")
#     print("")
#2  质数之和
# def zsh(x=2,y=100):
#     a = 0
#     for b in range(x,y):
#         for c in range(x,b) :
#             if b%c == 0:
#                 break
#         else:
#             a = b + a
#     print(a)
#zsh(x,y)
# #  阶乘之和
# def jc(x=5):
#     a = 1
#     b = 0
#     for i in range(1,x+1): #使用for循环求和
#         a = a * i           #阶乘是从1开始乘，一直乘到n
#         b = b + a         #把每个数的阶乘相加
#     print(b)
# jc(5)

# 4  判断三角形
# a = int(input("请分别输入第一条边：a== "))
# b = int(input("请分别输入第一条边：b== "))
# c = int(input("请分别输入第一条边：c== "))
# if a+b >= c and a+c >= b and b+c >=a :
#     if  a==b==c:
#         print("等边三角形")
#     elif a == c or a == b or b == c:
#         print("等腰三角形")
#     else:
#         print("这是一个三角形")
# else:
#     print("这不是一个三角形")

# a = int(input("井深："))
# b = int(input("白天："))
# c = int(input("晚上："))
# z  = 0#爬了多少
# f = 0#天数
# while a>0 :
#     z = z + b
#     f = f + 1
#     if z ==a :
#         print(f)
#         print("chulaila")
#     else:
#         z = z - c

#男人女人小孩共a人在一家饭店吃饭共花了b元，如果总共30人钱数50，别求出男人 女人 小孩多少人
# a = int(input("总人数：  "))
# b = int(input("总钱数：  "))
# for x in range(100):# x是男人
#     for y in range(100):# y是女人
#         for z in range(100):# z是小孩
#             if 3*x + 2*y + z == b:
#                 if x + y + z == a:
#                     print(x,y,z)
