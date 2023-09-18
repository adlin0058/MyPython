# 用正则表达式提取字符串中的 URL
import re


def findUrl(s):
    url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', s)
    return url


s = 'Runoob 的网页地址为：https://www.runoob.com，Google 的网页地址为：https://www.google.com'
print('Urls:', findUrl(s))
