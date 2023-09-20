
# todo  移除字典点键值(key/value)对
# 使用del

# dict = {"Runoob": 1, "Google": 2, "Taobao": 3, "Zhihu": 4}
# print('字典移除前：', dict)
# del dict['Zhihu']
# print('字典移除后：', dict)
# # 使用del移除不存在的项 会报错


# #! 使用pop
# dict = {"Runoob": 1, "Google": 2, "Taobao": 3, "Zhihu": 4}
# print('字典移除前：', dict)
# rmv_value = dict.pop('Zhihu')
# print('移除的value是：', rmv_value)
# print('字典移除后：', dict)
# # 使用pop移除不存在的项不会报错
# rmv_value = dict.pop('baidu', '没有该键')
# print(rmv_value)

#! 使用items()移除
dict = {"Runoob": 1, "Google": 2, "Taobao": 3, "Zhihu": 4}
print('字典移除前：', dict)
new_dict = {key: value for key, value in dict.items() if key != 'Zhihu'}
print('字典移除后：', new_dict)
