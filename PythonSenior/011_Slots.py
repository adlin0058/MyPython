
# todo 使用__slots__限定属性

class Student(object):
    __slots__ = ('name', 'age')


s = Student()
s.name = 'Michael'
s.age = 25

# s.score = 99

# 子类不受限制


class GraduateStudent(Student):
    pass


g = GraduateStudent()
g.score = 99
