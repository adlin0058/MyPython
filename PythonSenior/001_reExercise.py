
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
