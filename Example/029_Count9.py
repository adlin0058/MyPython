# 约瑟夫生者死者小游戏
# 报数，从 1 开始，数到 9 的人下船
# 直到船上仅剩 15 人为止
# 问都有哪些编号的人下船了呢
people = {}
for x in range(1, 31):
    people[x] = 1
# print(people)

# 用于循环遍历字典 1——31 值为31再次进入循环时会变为1
i = 1
# 用于报数 1-9 值为9时变为1
cnt = 0
# 用于计数下船几个
n = 0
while i <= 31:
    if i == 31:
        i = 1

    if people[i] == 0:
        i += 1
        continue
    elif people[i] == 1:
        cnt += 1
        if cnt == 9:
            people[i] = 0
            print(i, '下船')
            cnt = 0
            n += 1
        i += 1
    if n == 15:
        break
