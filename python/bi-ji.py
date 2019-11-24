# 字符串
# 1  .upper():将小写变大写
# a = 'abcd'.upper() #将小写变成大写
# g = 'abcd'.upper # 找到对应的存储位置
# # 2  .lower():将大写变小写
# print(input("请输入字符：").lower())
# a = 'ABCD'.lower()
# #3 .title():将首字母大写
# a = 'ab cd'.title()# 每个空格后的字母也大写
# print(a)
# # 4  .swapcase():大小写相互转换,把大写换成小写 把小写转成大写
# a = 'abcdEFG'.swapcase()
# print(a)
#5 将字符串中的字符替换为其他数据 .replace（‘原内容’，‘替换内容’，替换数量）
# a = 'aaaaa'
# c = 'aaaaa'
# b = a.replace('a','zz',1)#数量1指的是 替换里面一个 a，数量2指的是 替换里面两个a
# d = c.replace('a','zz')# 不加数字是全部替换
# print(b)
# print(d)
# #6  以括号中的数据为分隔符，将字符串分割成列表  .split( ‘分隔符’ )
# a = 'abcdefgabcdefgabcdefg'
# b = a.split('ab')#以 分隔符为界限，将内容分隔出来，自动用‘’ 括起来，自动用  ，号 分割开
# print(b)
#7 以某个数据将列表中的元素连接起来形成新的字符串  分隔符 . join （元素列表）
# a = ['abc' ,'defg' ]
# b = '-'.join(a)
# print(b)
# 6 与 7 连用
# a = 'abcdefgabcdefgabcdefg'
# b = a.split('ab')
# c ='*'.join(b)
# print(c)#将数字分割开，再连接起来
#8   .startswith(“字符串”) 判断是否以括号中的字符串为开头  (True 为 真，False 为假 )
# a = 'abcdefgabcdefgabcdefg'
# b = a.startswith('c')
# print(b)
#9  .endswith('字符串') 判断是否以括号中的字符串为结尾  (True 为 真，False 为假 )
# a = 'abcdefgabcdefgabcdefg'
# b = a.startswith('a') and a.endswith('g')
# print(b)
#10 字符串的三种格式化
#10.1 '%' %填的字符  %s 通过str（）将输进去的字符转化成字符串; %s只能填整数；%f只能填浮点数；
#10.2 '{}'.format()：格式化字符串
# a = '{}*{}={}'.format(5,6,5*2)
# print( '{}*{}={}'.format(5,6,5*2))
#10.3 f'{}' 将内容连起来打印
# a = '123'
# b = '456'
# print(f'{a}+{b}')

#11 .strip（）：去除字符串左右两边的字符
# a = 'abcdefga'
# b = a.strip("gfdcba")# 去除两边的字符，可以无序，但是要连起来，也可以去除重复的
# print(b)
# a = 'abcccdefga'
# b =  a.strip("abcfeg")#去除两边的字符，包括重复的，可以无序，但是要连起来
# print(b)
# a = 'abcdefga'
# b = a.lstrip("adcb")# 去除最左边的字符，可以无序，但是要连起来
# print(b)
# a = 'abcdefga'
# b =  a.rstrip("afeg")#去除最右边的字符，可以无序，但是要连起来
# print(b)
#12  .count():统计()中的字符在字符串中的数量
# a = 'abacadaeafaga'
# b = a.count('a')
# print(b)
#13  .index() 查看括号中字符串所在的下标位置
# a = 'abacada'
# b = a.index('a',1,10)# 找到从 1 开始 到 10 结束，第一个 a 的位置
# print(b)
# a = 'abacada'.index('a')# 找到从头开始 到最后结束，第一个 a 的位置
# print(a)
#14   len（） 统计右多少元素
# a = 'abcdefg'
# b = len(a)# 统计有多少 元素
# print(b)

#字符串用法
# a = ["A","B","C","D","E","F","G"]
# b = [85,95,34,65,84,56]
# print(len(a))#统计表中有几个数据
# print(a)#把表中 a 所有的值打印出来
# print(type(a))# 查看类型值
# a [3] ="d"#修改表中第4个值
# print(a[3])#找a表中的第 4个值
# for a in range (2,100): # 逐一 显示 2——99的值  不包括后面的100
#     print(a)  # 把表中 2——99的值打印出来
# b = 0
# while b <= len(a)-1:#a中的值减 1
#     print("下面有请 %s 出场" % a[b])# a表格中的第b个值，打印出来
#     b = b + 1
# print(a.index("A"))#找 表中数据所在位置
# a.append("H")# 在最后追加数据

# a.insert(0,"a")#在0处插入数据
# b.extend(a)#将a里面的数据追加到b数据后面
# a.clear()#清空列表内容
# a.remove("A") #移除表中数据
# print(a)
# a.pop(0)#根据下标数据 删除数据
# del a[0]
# print(a)#根据下标数据 删除数据（关键字）
# print(a.count(" "))#统计表中数据
# a.remove(" ")#移除表中数据，有两个值的话从前往后
# a.sort(reverse=True)#True 指的是 降序
# a.sort()#默认升序
# a.reversed() #逆序 从后往前打印
# a.sort(reverse=True)#True 指的是 降序
# a.sort()#默认升序

#更改类型
# a = 123
# a = str(a)
# print(type(a))
# print(a[1])
# #单引号 与 双引号
# a = "i'm a \"boy\""
# print(a)
# a = "i'm a 'boy'"
# print(a)

#  字符串类型
# # 1.只能0增加
# a = 'sde' + 's'
# print(a)
# # 2.支持索引
# a = ["A", "B", "C", "D", "E", "F", "G"]
# print(a[2])#从0开始
# print(a[-5])#最后一个为 -1
# # 3.支持切片
a = "ABCDEFG"
# #3.1将数字放在 冒号前
# print(a[2:])#显示内容 从数字所对应的字符开始直到最后结尾
# print(a[-2:])#显示内容 从后往前，负几 就是从后往前显示几个
# #3.2将数字放在 冒号后   （不包含冒号后的数字）
# print(a[:2])#显示 到 数字之前的内容（不包含数字所对应的内容）
# print(a[:-2])#显示到数字负数 所对应之前的内容（不包含数字所对应的内容）
# #3.3冒号在中间
# print(a[2:-2])#显示从数字开始 （包含数字） 到 负数结束 （不包含负数）
# print(a[-5:-1])#显示从负数字开始 （包含数字） 到负数结束 （不包含负数）
# #4 两个冒号时
# a = "AB CD EF GH IJ KL MN HO PQ RSTUVWXYZ"
# #4.1 将下标号放在冒号前
# print(a[-2::])#显示最后到数字负数 所对应之前的内容（包含数字所对应的内容）
# print(a[2::])#显示从下标号对应的字符开始到结尾（包括下标号）
# #4.2 将下标好放在冒号后
# print(a[::2])#以下标号为一组，默认显示 第一个内容
# print(a[::-2])#以下标号为一组，以倒序方式 默认显示 第一个内容
# #4.3 冒号在中间
# print(a[2::4])#以下标号（例：4）为一组，显示每一组的第2个内容
# print(a[3::2])# 如果前面数字比后面大，就会从0开始数第（例：6）个开始，显示以下标号（例：2）为一组的第一个内容
# a = "ABCDEFG"

#1   for 循环
# 列表不加 range，列表有自己的下标顺序
#range 把数字变成范围
# for i in "13265871":
#     print(i) #将i内的数字挨个循环
# #1.1   break 终止循环
# for a in 'abcdefg':
#     if a == "d" :#到d 就直接结束
#         break
#     print(a)
# else:
#     print(666)
# #1.2   continue 终止本次循环，执行下一次循环
# for a in 'abcdefg':
#     if a == "d" :
#         continue
#     print(a)
# else:
#     print(666)

#10.15
# 字典
#字典能 存储各种各样的数据
# 格式：由键值对组成
# 变量名={key1：valuel,
#        key2:  0value2,}
# 特点：1.无序的、2.键必须是唯一的3.不支持索引 4.可变的
# a = {
#     'name' : '张三',
#     'age':[19,20,21],
#     'sex':{'nan':23,'age':98}
#     }
# a.popitem()# 默认删除最后一个
# a.pop('age')# 根据键来删除字典中的数据
# print(a.keys())# 获取所有的key
# print(a.values())#获取所有的值
#print(a.items())#获取所有的键值对
# b = {'www':666}
# a.update(b)# 把 b 中的数据更新到 a 中
# print(a)

#  str,list,tuple,dict,bool:布尔值,int,float,set,None：空值（不等于0）
#set（集合）  格式 ：变量名 = {数据1，数据2，数据3，....}
# 特点 ： 1.无序的、不重复的（值不会重复）   2. 不支持索引和切片  3. 可变的
# a = {123,123,56,46,9684665,652,22,22,22,5}
# #添加数据
# a.add(66666666)# 添加数据
# a.remove(123)# 删除指定数据
# a.pop()#随机删除数据

# & 交集  - 差集   | 并集
#print(a & b)(a | b)(a-b)
#定义一个空集合  c = set()  （集合的写法和字典很相似）
#range  把数字变成范围  列表不用要range
# for  变量名  in 范围   范围：有序列的数据
# enumerate：将有序列的数据的下标位置和对应的数据 对应显示出来
# for 变量 in enumerate( )
# a = [13,12,15,56,98,54,65,45]
# for i,j in  enumerate(a):
#     print(i,j)
# # items 将字典里面的 键与值 分别取出来
# b = {'name':888,'age':666}
# for i , j in b.items():
#     print(i,j)

# 10.16
# 列表推导式
#将条件控制语句写在列表中，产生的结果会自动存储在列表中
#格式： [语句的结果   条件控制语句]
#1 计算10以内的每个偶数的平方
# b = [i**2 for i in range(2,11,2)]
# print(b)
#2 用列表推导式 将大于55 的放一起 小于55 的放一起
# a = [11,22,33,44,55,66,77,88,99,110,120]
# b = [b  for b in a if b>55 ]
# print(b)
# #3 sum 求和 指的是 整数
# a = sum(range(2,101,2))
# print(a)
# print(sum(range(1,101,2)))

#1 函数
#具有某种功能的 可重复使用的代码块
# 作用：节省代码，重复使用
# 格式： def  函数名()：
#                执行语句块
#函数名的命名规则 和 变量名的命名规则一样 ，不能随便写
# 调用函数方法：
# 函数名（）
#1 例：
# def jishuhe():
#     a = sum(range(1,100,2))
#     print(a)
#
# jishuhe()
#2 变量的作用域
#局部变量： 只在函数内有用的变量            （只在一小块区域内有用）
#全局变量： 在整个python文件中都可以使用的   （在任何区域内都可以使用的）
# global 变量名   将局部变量变成全局变量
# def oushuhe():
#     global o# global 变量名   将局部变量变成全局变量
#     o = sum(range(2,101,2))
#     print(o)
# oushuhe()

#3 参数传递 优先级： 必须参数 > 默认参数 > 可变长参数
#3.1 必须参数  必须填写的参数
#参数名的规则和变量名的规则一样
#格式： def    参数名 （参数名）
#                 执行语句块
# 例:
# def he(x,y):
#     a = sum(range(x,y+1))
#     print(a)
#调用
# he("参数"，"参数")
#3.2 默认参数   当调用函数时，传入数据时，就使用传入数据；如果不传入数据时，就使用默认值
#格式： def    参数名 （参数名 = 值）
#                 执行语句块
# 例:
# def he(x=100,y=1000):
#     a = sum(range(x,y+1))
#     print(a)
# print(a)
# # 调用
# he()

#3.3 可变长参数（默认写法： *args ）   一次性可以接收很多数据  接收到的数据是元组
#格式：   def  函数名（*参数名）：
#                 print(x)
#例：
# def qq(*args):
#     print(args)
# qq('asdfadfa',['asdxfsad'],{'asd':'asd',ascii:'sqs'})
# qq('sdgtsgsegsegsegsefsg',('arrarawawrrawrawrar'))
# 3.4  可变长参数（默认写法： *kwargs ）传入数据 必须是键值对格式，接收到的数据类型是 字典
# 格式： def 函数名（**参数名）：
#                 执行语句块
#例：
# def qq(**kwargs):
#     print(kwargs)
# qq(asd='asd',ascii='sqs')# 必须是字典的写法


#4 return  返回值
#     作用：1.将return 后面的 数据赋值给函数
#          2.结束函数
# 格式：      def   函数名（）

#10.18
#  None  空值
#嵌套函数
# def  hanshu():
#     a = 123
#     print(a)
#     def hanshu2():
#         b = 456
#         return b
#     return hanshu2()
# print(hanshu())# hanshu()是一个空值，但是他下面的却有值

#匿名函数
# a = lambda  x,y : x + y#  冒号后面是表达式
# print(a)#打印出来是位置
# print(a(6,19))#打印出来是 值
# a = lambda x,y:x+y  if x==y else 6666
# print(a(121,22))
# a = lambda x,y:x+y [i for i in range(10) if i < 5]
# a = lambda *c :print()
# a(121)

#系统函数
#1 enumerate( ) : 将有序列的数据中的值与其下标显示
# for i,j in enumerate('abcd'):
#     print(i,j)
#2 sum 求和函数（ 括号中 只能填元组，列表，集合）
# a = sum({2,4,8,10})
# print(a)
#3 max()  找 最大，必须是同种类型
# a = max('3a','6z','9g')#按照前面的来排序
# print(a)
#4 min（） 找 最小，必须是同种类型
# a = min('a9','z6','g3')#按照前面的来排序
# print(a)
#5 divmod()
# a,b = divmod(60,7)
# print(a,b)# a 为商 ， b 为余数
#6 chr() 将 码 转换为ascii 码中的值
# a = chr(65)
# print(a)
# a = [chr(i) for i in range(65,91)]#大写字母
# a = [chr(i) for i in range(97,123)]#小写字母
#7 ord  将值转换为ascii码
# a = ord('a')
# print(a)
#8 bin() 将 10 进制转换成 2 进制
# a = bin(66)
# print(a)#0b 指2进制
# b = bin(67)
# print(b)
#9 oct()将 10 进制转换成 8 进制
# a = oct(8)
# print(a)#0o 指8进制
# b = oct(7)
# print(b)
#10 hex()将 10 进制转换成 16 进制
# a = hex(16)
# print(a)#0x 指16进制
# b = hex(17)
# print(b)
#11 int()将 任意进制转换成 10 进制
# a = int(0o10)# 前面要加上 相对于的 标识
# print(a)

# try:# 如果try 错误了，就执行 except  语句
#     int(a)
# except NameError :
#     print("定义错误")
# except ValueError :
#     print("值错误")

# try:
#         list(66)
#         print(666)
# except Exception as f:
#     print(66)
#     print(f)
# except ValueError as b:
#     print(b)
# except Exception as h :# 所有异常错误
#     print(h)
# else:
#     print("执行else语句")
#finally:
  #  print("执行了finally语句")

# raise TypeError('这是类型错误')

# try:
#     s = None
#     if s is None:
#         print("s shi kong de ")
#         raise NameError ('as 相当于 执行了raise 后面的') # 告诉系统受到异常信号 相当于认为制造了一个异常
#     print(3333333333)          # 在raise后面的语句不再执行。
# except Exception as d:
#     print("8888888888888")
#     print(d)

# raise TypeError('123456')  # 自定义错误显示


#类的专有方法
# class lei():# 类的专有方法
#     def __init__(self, nabc, xabc=100):#  给类传参数，添加属性
#         self.Nabc = nabc #前面命名必须大写
#         self.Xabc = xabc #添加属性
#     def __str__(self):#辅助类 为了结果更好看
#         ta =  '我：' + self.Nabc + '\n'
#         ta += '你: '+str(self.Xabc) + '\n'
#         return ta # 返回值
#     def hanshu(self,a,b=10,*args,**kwargs):# 可以添加各种类型 ，以及下面式子的类型
#         # 可以用  =  -=  +=   *  /  各种函数和各种循环
#          print(a,kwargs)
# a = lei('小明')# 给类传参数，添加属性
# a.hanshu(123,age=100)# 给函数传参，添加函数内容
# print(a)

# 私有方法
# class lei():
#     def diaoyong1(self):
#         return self.__diaoyong2()#函数前加 ———  为私有方法，在内部可用
#     def __diaoyong2(self):
#         a = 666
#         return a
# a = lei()
# print(a.diaoyong1())
#a.diaoyong2()# 函数前面加 ———  为私有方法，在外部不可用

# a = 1
# print("%d%%"%a)

# # zip 函数
# a = [1,2,3,4,5]
# b = ['1','2','3','4']
# yasuo = zip(a,b)
# for i , j in yasuo:
#     print(i,j)
#
# # 追加 内容
#     with open(r'c:\Users\369\Desktop\xioashuo.txt', 'a', encoding='utf-8') as f:
#         f.write('\n' + '\t' * 6 + '内容' + '\n')
#         f.write('内容')

