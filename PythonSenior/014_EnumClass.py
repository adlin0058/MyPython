
# from enum import Enum

# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May',
#              'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)


from enum import Enum, unique


# # unique装饰器可以帮助我们检查保证没有重复值
# @unique
# class Weekday(Enum):
#     Sun = 0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6

# todo 把Student的gender属性改造为枚举类型，可以避免使用字符串
class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, Gender):
        self.name = name
        self.gender = Gender
