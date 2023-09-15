# 约瑟夫生者死者小游戏
# 报数，从 1 开始，数到 9 的人下船
# 直到船上仅剩 15 人为止
# 问都有哪些编号的人下船了呢

people = {}
for x in range(1, 31):
    people[x] = 1

# print(people)
cnt = 0
x = 0
while cnt < 15:
    if people[x] == 1:
        if cnt == 9:
            people[x] = 0
            print(x, '号下船了')
            cnt += 1
        x += 1
