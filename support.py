#!/sur/bin/python3
# Filename: support.py

if __name__ == '__main__':
    print('程序自身在运行')
else:
    print('我来自另一个模块')

    def print_func(par):
        print('Hello :', par)
        return
