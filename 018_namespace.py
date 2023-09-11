
#! 命名空间和作用域

# # var1是全局名称
# var1 = 5


# def some_func():
#     # var2是局部名称
#     var2 = 6

#     def some_inner_func():
#         # var2是内嵌的局部名称
#         var3 = 7


#! 全局变量和局部变量

# total = 0  # 全局变量


# def sum(arg1, arg2):
#     # 返回2个参数的和
#     total = arg1 + arg2  # total在这里是局部变量
#     print('函数内是局部变量：', total)
#     return total


# sum(10, 20)
# print('函数外的是全局变量：', total)


a = 10


def test():
    global a
    a = a + 1
    print(a)


test()
