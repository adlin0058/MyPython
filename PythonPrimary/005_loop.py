# names = ['Michael', 'Bob', 'Tracy']
# for name in names:
#     print(name)

# sum = 0
# for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     sum = sum + x
# print(sum)


# print(list(range(5)))

# todo 计算1-100的整数和
# sum = 0
# for x in range(101):
#     sum += x
# print(sum)


# todo 计算100以内所有奇数之和
# sum = 0
# n = 99
# while n > 0:
#     sum = sum + n
#     n = n - 2
# print(sum)

# todo 对每个人打招呼
# L = ['Bart', 'Lisa', 'Adam']
# for name in L:
#     print(f'Hello , {name}!')

# todo 打印1-10
# n = 1
# while n <= 100:
#     if n > 10:
#         break
#     print(n)
#     n = n + 1
# print('END')

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:  # 如果n是偶数，执行continue语句
        continue  # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
