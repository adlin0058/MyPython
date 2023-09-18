# key排序
def sortKey(d):
    print('key排序：')
    for i in sorted(d):
        print((i, d[i]), end=" ")
    print()

# value排序


def sortValue(d):
    print('Value排序：')
    print(sorted(d.items(), key=lambda kv: (kv[1], kv[0])))
    print()


def main():
    d = {2: 'm', 1: 'l', 4: 's', 3: 'z'}
    sortKey(d)
    sortValue(d)


if __name__ == "__main__":
    main()
