

# ! 多重继承
# 动物类
class Animal(object):
    pass

# 哺乳类和鸟类


class Bird(Animal):
    pass


class Mammal(Animal):
    pass

# 能跑的和会飞的


class Flyable(object):
    def fly(self):
        print('Flying...')


class Runnable(object):
    def run(self):
        print('Running...')


# 狗类 哺乳、会跑
class Dog(Mammal, Runnable):
    pass

# 蝙蝠类 哺乳、会飞


class Bat(Mammal, Flyable):
    pass

# 鹦鹉类 鸟类、会飞


class Parrot(Bird, Flyable):
    pass

# 鸵鸟类 鸟类、会跑


class Ostrich(Bird, Runnable):
    pass
