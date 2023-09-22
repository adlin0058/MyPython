# 杨辉三角

def triangle():
    yield (result := [1])
    while True:
        yield (result := [a+b for a, b in zip(result + [0], [0]+result)])
