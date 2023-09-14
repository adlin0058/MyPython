# fibonacci

def fib(n):
    n1 = 0
    n2 = 1
    cnt = 2
    if n < 0:
        print('请输入一个正数')
    elif n == 1:
        print(n1)
    else:
        print(n1, ',', n2, end=' , ')
        while cnt < n:
            nt = n1 + n2
            print(nt, end=' , ')
            n1 = n2
            n2 = nt
            cnt += 1
        print()


# fib(1)
fib(10)
# fib(5)
