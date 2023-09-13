# 判断闰年
""" 
1. 整百年 year % 100 == 0
    1.1 是400的倍数(闰年) year%400 == 0
    1.2 不是400的倍数
2. 非整百年 year % 100 != 0
    2.1 是4的倍数(闰年) year%4 == 0
    2.2 不是4的倍数
"""


def isLeap(y):
    try:
        if y % 100 == 0:
            if y % 400 == 0:
                print('%d 年是闰年' % y)
            else:
                print('%d 年不是闰年' % y)
        else:
            if y % 4 == 0:
                print('%d 年是闰年' % y)
            else:
                print('%d 年不是闰年' % y)
    except Exception:
        print('输入错误')


isLeap('1900')
isLeap(1998)
isLeap(1996)
isLeap(2000)
