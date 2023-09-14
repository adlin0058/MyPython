# 文件IO

with open('/home/lm/MyPython/Example/025_Test.txt', 'wt') as out_file:
    out_file.write('该文本会写入到文件中\n看到我了吧:)')

with open('/home/lm/MyPython/Example/025_Test.txt', 'rt') as in_file:
    text = in_file.read()

print(text)
