# def foo():
#     r = some_function()
#     if r == (-1):
#         return (-1)

# def bar():
#     r = foo()
#     if r == (-1):
#         print('Error')
#     else:
#         pass


# #! try

# try:
#     print('try...')
#     r = 10/0  # * 错误，进行跳转
#     print('result:', r)
# except ZeroDivisionError as e:  # * 跳转到
#     print('except:', e)
# finally:
#     print('finally...')
# print('END')

# try:
#     print('try...')
#     r = 10/int('a')
#     print('result:', r)
# except ValueError as e:
#     print('except:', e)
# except ZeroDivisionError as e:
#     print('except:', e)

# finally:
#     print('finally...')
# print('END')


# try:
#     print('try...')
#     r = 10/int('2')
#     print('result:', r)
# except ValueError as e:
#     print('except:', e)
# except ZeroDivisionError as e:
#     print('except:', e)
# else:
#     print('no error')
# finally:
#     print('finally...')
# print('END')


# try:
#     foo()
# except ValueError as e:
#     print('ValueError')
# # * UnicodeError 是 valueError的子类
# except UnicodeError as e:  # ! 永远不会执行
#     print('UnicodeError')

# import logging


# def foo(s):
#     return 10 / int(s)


# def bar(s):
#     return foo(s) * 2


# def main():
#     # bar('0')
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)


# main()


from functools import reduce


def str2num(s):
    return float(s)


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


main()
