#! \usr\bin\python
#-*-coding:utf8_*-

import xlwt
import xlrd
import xlutils
from xlutils.copy import copy  # 引用copy 模块


# 导入模块0
# 1  写入 excel 文件的格式
geshi = xlwt.Workbook(encoding='utf-8') #xlwt.Workbook()是产生一个空文件的对象
# 2   创建标签页( 可以多个) cell_overwrite_ok=True 表示单元格可以 重新设值
sheet = geshi.add_sheet('py_1906',cell_overwrite_ok=True)
# sheet1 = geshi.add_sheet("py_1026")#.add_sheet（）为空文件对象，是在该文件中建立一个工作表
# 3  写入内容  ,第一个数字代表行，第二个数字代表列


# ，第三个代表内容
# sheet.write(0,1,'中国')
# sheet.write(0,1,'779')

# 写入九九乘法表
# for a in range(10):
#     for b in range(1,a+1):
#         c = a*b
#         sheet.write(a-1,b-1,'%d*%d=%d'%(a,b,c))

# 在 txt文件中 写入东西
# txt = open(r'c:\users\369\desktop\ccc.txt','w',encoding='utf-8')
# for a in range(10):
#     for b in range(1,a+1):
#         txt.write(f'{a}*{b}={a*b} \t')  # \t 指的是 间隔空
#     txt.write('\n')  # 换行
# txt.close()

# #  将 txt 文件 写入到 excel 文件中
a = open(r'c:\users\369\desktop\ccc.txt','r',encoding='utf-8')
b = a.readlines()
a.close()

for i in range(len(b)):
    c = b[i].split()
    for j in range(len(c)):
        sheet.write(i,j, c[j])

# # 保存 并 命名文件名（）
geshi.save('my_excel.xls')
# geshi.save("my_xinexcel.xls")

# 完整的步骤  #
# import xlwt  #导入模块
# geshi = xlwt.Workbook(encoding='utf-8')   # 格式
# a = geshi.add_sheet('py_10.28')   # 命名标签页
# a.write (0,1,'表格666')  # 写入 数据
# for i in range(10):
#     for j in range(1,i):
#         a.write(i,j,'%d*%d=%d'%(i,j,i*j))  # 写入数据
#         a.write(i,j,'{}*{}={}'.format(i,j,i*j))
# geshi.save('py_10.28.xls') # 关闭并命名文件名

# import xlrd
# 打开 读取文件
# wenjian = xlrd.open_workbook('my_excel.xls')
# 第一种方法
# 统计有多少个标签页
# a = wenjian.nsheets   # nsheets 统计有多少个标签页
# print(a)
# 通过索引值进入标签页
# b = wenjian.sheets()[0]
# print(b)

# # 查看 我们进入的标签页里的格子的内容
# gezi = b.cell(0,1).value
# print(gezi)

# 第二种方法
# import xlrd
# 打开 读取文件
# wenjian = xlrd.open_workbook('my_excel.xls')
# 获取excel 里的所有标签页的名称
# a = wenjian.sheet_names()
# print(a)
# 通过名字 进入标签页
# b = wenjian.sheet_by_name('py_1906')
# 获取第一个格子里的值
# gezi = b.cell(0,0).value
# print(gezi)

#  查看文件中行和列
# 获取标签页中总共有多少行 （ 以列表形式）
# hang = b.nrows
# print(hang)
# 获取 标签页 中 第几行内容 （ 以列表形式）
# hang_neirong = b.row_values(6)
# print(hang_neirong)
# 循环显示 出 表格中 行 的内容
# for i in range(hang):
#     hang_neirong = b.row_values(i)[0]
#     print(hang_neirong)

# 获取标签页中总共有多少 列 （ 以列表形式）
# lie = b.ncols
# print(lie)
# 获取 标签页 中 第几 列 内容 （ 以列表形式）
# lie_neiRong = b.col_values(0)[1]
# print(lie_neiRong)
# 循环显示出 表格中 列 的内容
# for i in  range(lie):
#     lie_neiRong = b.col_values(i)
#     print(lie_neiRong)


# 将 excel 中内容 导入到txt 中
# txt = open(r'c:\users\369\desktop\ccc.txt','w',encoding='utf-8')
# for i in range(1,10):
#     z = b.cell(i,0).value   # 循环获取格子里的值
#     txt.write('\n')
#     txt.write(z)
# txt.close()

import xlutils
from xlutils.copy import copy  # 引用copy 模块
# import xlrd
# 文件等于一个值
# z = xlrd.open_workbook('my_excel.xls')
# 复制文件，不是直接打开excel文件，而是复制一份操作的文件，只有写的操作，没有读取的操作
# New_z = copy(z)
# get_sheet(下标位置)，根据下标位置进入相对应的标签页
# bqy = New_z.get_sheet(0)
# 增加内容
# bqy.write(1,1,'内容')
# 保存 到以前文件（）
# New_z.save('my_excel.xls')
# 保存 另存为 新的文件
# New_z.save('xinde_excel.xls')
