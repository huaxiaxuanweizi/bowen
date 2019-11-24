#！/usr/bin/python
#-*-coding:utf8-*-

"""
1. python 介绍 3.0 创始人
编程语言：java 、 c 、c++ 、 c# 、 php 、 python
编程语言：   编译型：源代码——编译器——二进制——可执行文件
            解释型：源代码——解释器——字节码——编译器——可执行文件

2. 解释器 和 编辑器
解释器：解释python代码     类似于 cpython、jpython 官网上下载 默认的是cpython解释器
编辑器：书写python代码的   类似于 pycharm、sublime text

3. 搭载环境 安装python 安装pycharm
勾选 add 选项  或 属性 高级系统设置  环境变量 新建

4. 循环语句
while 条件： 条件：非0即为真，加执行语句块
while  else  ：只要循环不被 break 掉，就执行 else 语句
for 循环 ：  格式：  for 变量名  in 范围
                        范围指 ：有序列的数据，即按照一定的顺序排列。即有下标顺序：元组 列表 字符串
range（）:将数字变成范围，3个值 开始值，结束值，递进值
enumerate：将有序列的数据的下标位置与值 相对应
for else ：只要循环不被 break 掉，就执行 else 语句
break    continue

5. 判断语句
if  条件1  elif 条件2  else：

6. 语句块
注意：  1. 缩进  2. 冒号

7. 数据类型
str list tuple dict set int float bool time None
可变 不可变 指的是 内存位置

8. 执行文件的 py方式
1. python  文件名
2. 在文件的路径上 输入cmd 进去后再输入 文件名
3. 选择打开方式 选择 python打开

9. 列表推导式
10. 函数  具有某种功能的，可重复使用的代码块
def  函数名：
定义函数
global 变量的作用域
参数传递：必须、默认、可变长
return  用法
lambda  匿名函数

11. 对文件的操作
open 函数（r'文件'，权限，编码方式）
with 语句 ：上下文管理器   自带 _enter_ 与 _exit_

12. 模块的使用
下载1.  pip  2. pycharm  3. 源码安装

from  包名.模块名  import 函数名
from  包名.模块名  import *   *代表这个模块的所有函数都能用
from  模块名  import 函数名

import 模块名
函数

#判断正在执行的文件 是不是本文件
if _name_ == '_main_':
_name_ 获取内存中，执行的文件名
_main_ 指 在本文件执行，如果在别的文件执行，就是本文件的模块名

13 异常
try、 except、 else、 finally
raise 自定异常


14 面向对象：将函数进行分类、封装，使开发更高效
    面向过程：性能高（快）
类：方便管理，更好更快的去调用
    方法：功能
    self：类的实例，方便在类的内部调用
    封装：将代码写在类中
    继承：新的类可以继承旧类中所有的函数
    多态：方法重写
    专有方法： _ init _ 给类传参
    私有方法：在 函数左边加两个 __
    私有属性：在属性前面加两个 __
15. json
json： 一种轻量级的数据交互格式
作用：存储数据
格式：等同于字典
java Script 语言的一种格式，用于网站内容的传输
 将字典转换成 json字符串格式
json.dumps()
将json字符串转换成字典
json.loads()



"""


