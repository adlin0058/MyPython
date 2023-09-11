
# todo 摄氏温度转华氏温度

celsius = float(input('输入摄氏温度：'))

fahrenheit = (celsius * 1.8) + 32
print('%0.1f 摄氏温度转为华氏温度为 %0.1f' % (celsius, fahrenheit))

# todo 华氏温度转摄氏温度

fahrenheit = float(input('输入华氏温度：'))

celsius = (fahrenheit - 32)/1.8

print('%0.1f 华氏温度转摄氏温度为 %0.1f' % (fahrenheit, celsius))
