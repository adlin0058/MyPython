# filter()与map()类似，接收一个函数和一个序列
# 不同的是flter()的函数将作用于序列的每一个元素
# 然后根据返回值是true或false决定元素的舍弃和保留

# # todo 删除序列中的偶数
# def is_odd(n):
#     return n % 2 == 1


# l = list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(l)


# # todo 序列中的字符串删掉
# def not_emple(s):
#     return s and s.strip()


# l = list(filter(not_emple, ['A', '', 'B', None, 'C', '   ']))
# print(l)


# todo 用filter求素数
# 构造一个从3开始的奇数序列，2以上的偶数不会是素数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)


# ? 打印1000以内的素数
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
