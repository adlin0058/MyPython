
#! Python中switch的实现
seasondict = {
    1: "Spring",
    2: "Summer",
    3: "Fall",
    4: "Winter"
}


def getSeason(season):
    """
    将season映射为字符串
    :param season:
    :return:
    """
    return seasondict.get(season, "Invalid Season")


print(getSeason(2))
