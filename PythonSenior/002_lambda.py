# def multiply(x, y): return x*y


# print(multiply(4, 2))

# print((lambda x, y: x*y)(4, 2))

# title = "HelloPython"
# (lambda title: print(title))(title)


# numbers = [50, 29, 41, 6, 1, 32]

# result = filter(lambda x: x > 10, numbers)
# print(list(result))


# numbers = [23, 634, 12, 62, 71, 23, 61, 72]
# result = map(lambda x: x**2, numbers)
# print(list(result))

# #! reduce()
# from functools import reduce
# numbers = [2, 32, 51, 56, 2, 82, 21]
# print(sum(numbers))
# rst = reduce(lambda x, y: x+y, numbers)
# print(rst)

#! sort()
cars = [
    ('mazda', 2000),
    ('toyota', 1000),
    ('benz', 500)
]
print(sorted(cars, key=lambda car: car[1]))
