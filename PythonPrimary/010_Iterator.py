# 迭代器

#! 创建
# list = [1, 2, 3, 4]
# it = iter(list)
# print(next(it))
# print(next(it))
# print(next(it))

#! 迭代器对象可使用常规的for语句遍历
# list = [1, 2, 3, 4]
# it = iter(list)
# for x in it:
#     print(x, end=" ")
# print()


#! 也可以使用next()函数遍历
# import sys
# list = [1, 2, 3, 4]
# it = iter(list)  # * 创建迭代器对象

# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()


#! 把类作为迭代器
# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self

#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x


# myclass = MyNumbers()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))


#! 异常标识符StopIteration
# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self

#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration


# myclass = MyNumbers()
# myiter = iter(myclass)

# for x in myiter:
#     print(x)


#! 生成器
# def countdown(n):
#     while n > 0:
#         yield n
#         n -= 1


# # 创建生成器对象
# generator = countdown(5)

# # 通过迭代生成器获取值
# print(next(generator))
# print(next(generator))
# print(next(generator))

# # 使用for循环迭代生成器
# for value in generator:
#     print(value)


#! 使用yield实现斐波那契数列
import sys


def fibonacci(n):  # 生成器函数
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a+b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
