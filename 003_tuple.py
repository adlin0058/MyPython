# tuple 是无法修改的list
t = ('a', 'b', ['A', 'B'])
print(t[0])
print(t[2][0])
t1 = ()
t2 = (1,)
