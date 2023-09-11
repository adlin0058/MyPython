
#! Python3标准库

# #! 操作系统接口
# import os

# # 返回当前工作目录
# print(os.getcwd())

# # 修改当前的工作目录
# # os.chdir('/server/accesslogs')

# # 执行系统命令 mkdir
# # os.system('mkdir today')

# #! glob模块
# import glob
# # 从目录中根据通配符搜索并产生文件名称列表
# print(glob.glob('*.py'))


# #! datatime模块
# import datetime

# # 获取当前日期和时间
# current_datetime = datetime.datetime.now()
# print(current_datetime)

# # 获取当前日期
# current_date = datetime.date.today()
# print(current_date)

# # 格式化日期
# formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
# print(formatted_datetime)


# #! 性能度量
# from timeit import Timer
# t1 = Timer('t=a;a=b;b=t', 'a=1;b=2').timeit()
# print(t1)
# t2 = Timer('a,b = b,a', 'a=1;b=2').timeit()
# print(t2)


#! 测试模块
import doctest


def average(values):
    """
    >>> print(average([20,30,70]))
    40.0
    """
    return sum(values)/len(values)


doctest.testmod()
