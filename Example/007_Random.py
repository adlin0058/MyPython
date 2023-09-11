# 随机数生成

import random

# todo 输出介于0.0和1.0之间的整数
random_number = random.random()
print(random_number)

# todo 输出介于0和10之间的整数（包含0和10）
random_int = random.randint(0, 10)
print(random_int)

# todo 从序列中随机选择一个元素
list1 = [1, 2, 3, 4, 5, 6]
random_element = random.choice(list1)
print(random_element)

# todo 将序列中的元素随机排列
random.shuffle(list1)
print(list1)
