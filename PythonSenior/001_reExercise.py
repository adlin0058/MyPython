
# todo 写一个验证Email地址的正则表达式

""" 
    someone@gmail.com
    bill.gates@microsoft.com
"""
import re
re_email = re.compile(r'^(\w+)([\.\-\+]\w+)*@(\w+)(\.\w+)+$')


def is_valid_email(addr):
    if re_email.match(addr):
        print('yes')
    else:
        print('no')


is_valid_email('someone@gmail.com')
is_valid_email('bill.gates@microsoft.com')
is_valid_email('bob#example.com')
is_valid_email('mr-bob@example.com')


# todo 提取出带名字的email地址
""" 
    <Tom Paris> tom@voyager.org => Tom Paris
    bob@example.com => bob

 """
re_name = re.compile(r'(?:<(.*)>)?\s*(\w+)@\w+(\.\w+)+')


def name_of_email(addr):
    n = re_name.match(addr)
    if n is None:
        return None
    if n.group(1) is not None:
        return n.group(1)
    return n.group(2)


n = name_of_email('bob@example.com')
print(n)
m = name_of_email('<Tom Paris> tom@voyager.org')
print(m)
