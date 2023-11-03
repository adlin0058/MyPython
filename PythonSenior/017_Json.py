
import json
# d = dict(name='Bob',age=20,sorce=80)
# str = json.dumps(d)
# print(str)
# a = json.loads(str)

# print(a)


#todo 将类序列化
class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

# 将类转化为字典的函数
def student2dict(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score
    }
      
s = Student('Bob',20,88)
#序列化成字符串
str = json.dumps(s,default=student2dict)
print(str)