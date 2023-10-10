
# class Student(object):
#     def get_score(self):
#         return self._score

#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value


# s = Student()
# s.set_score(60)
# print(s.get_score())

# # todo 使用@property装饰器简化

# class Student(object):

#     @property
#     def score(self):
#         return self._score

#     @score.setter
#     def score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value


# todo 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution

class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be an integer!')
        if value < 0 or value > 99999:
            raise ValueError('width error')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be an integer!')
        if value < 0:
            raise ValueError('width error')
        self._height = value

    @property
    def resolution(self):
        return (self._height) * (self._width)


s = Screen()
s.height = 99
s.width = 999
print(s.resolution)
