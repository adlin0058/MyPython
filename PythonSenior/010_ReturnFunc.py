
# todo 函数作为返回值
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


f = lazy_sum(1, 3, 5, 7, 9)
# 返回求和函数
print(f)
# 调用f时才计算求和结果
print(f())
