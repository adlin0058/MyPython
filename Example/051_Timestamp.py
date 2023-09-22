# 将字符串时间转换为时间戳

import time
a1 = '2023-9-21 16:56:00'
# 时间数组
timeArray = time.strptime(a1, '%Y-%m-%d %H:%M:%S')

print(timeArray)

# 时间戳
timeStamp = int(time.mktime(timeArray))
print(timeStamp)

# 转换格式
a2 = time.strftime('%Y/%m/%d %H:%M:%S', timeArray)
print(a2)
