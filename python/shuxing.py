#！/usr/bin/python
#-*-coding:utf8-*-

#创建类
#类 两种  1. 经典类：class Dog 广度搜素    2.新式类：class Dog（object）深度搜索
# class Dog(object):#类名  首字母大写
#     def run(self):#属性
#         print("跑")#方法
#     def pee(self):
#         print("上厕所")
     # def info(self):
#         self.pee()
#         self.run()
#         print(self.name)
#         print(self.color)
#         print(self.weiba)
# bigDog=Dog() #创建一个叫大狗的对象
# bigDog.name="大狗"# 类的实例
# bigDog.color="黄色"
# bigDog.weiba="有尾巴"
# bigDog.info()
# bigDog.pee()
# bigDog.run()

# class  Newdog(Dog):# 继承类
#     pass# 通过
# xiaogao=Newdog()
# xiaogao.run()
# xiaogao.pee()

# 重写
# class Ren(object):
#     def zou(self):
#         print("走")
#     def chi(self):
#         print("吃")
# class Daren(Ren):
#     def zou(self):
#         print("飞飞")
# dada=Daren()
# dada.zou()
# dada.chi()

# 多态
# import abc
# class  Animal(metaclass=abc.ABCMeta):
#     @abc.abstractclassmethod
#     def talk(self):
#         pass
# class Animal():#制定统一的类
#     def talk(self):
#         pass
# class People(Animal):# 人
#     def talk(self):
#         print("hello,nihao")
# class Pig(Animal):# 猪
#     def talk(self):
#         print("hengheng")
# class Dog(Animal):# 狗
#     def talk(self):
#         print("wnagwang")
# def trunk(obj):#定制统一接口
#     obj.talk()
# trunk(People())

#专用方法
# class Dog():
#     def __init__(self,color,weiba):
#         self.Color=color
#         self.Weiba=weiba
#         print(self.Color)
#         print(self.Weiba)
#     def pee(self):
#         print("厕所",self.Weiba)
# xiaogou=Dog('黄色','有尾巴')
# heigou=Dog('黑色','有一个尾巴')
#
# xiaogou.pee()
#类的专有方法
class lei():# 类的专有方法
    def __init__(self, nabc, xabc=100):#  给类传参数，添加属性
        self.Nabc = nabc #前面命名必须大写
        self.Xabc = xabc #添加属性

    def __str__(self):#辅助类 为了结果更好看
        ta =  '我：' + self.Nabc + '\n'
        ta += '你: '+str(self.Xabc) + '\n'
        return ta # 返回值

    def hanshu(self,a,b=10,*args,**kwargs):# 可以添加各种类型 ，以及下面式子的类型
        # 可以用  =  -=  +=   *  /  各种函数和各种循环
         print(a,kwargs)
a = lei('小明',666)# 给类传参数，添加属性
a.hanshu(1,age=100)# 给函数传参，添加函数内容
print(a)

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