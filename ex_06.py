# 测试模块1

# 全局变量
title = "模块1"

# 函数
def say_hello():
    print("我是 %s" % title)


# 类
class Dog(object):
    pass

if __name__ == "__main__":
    print("这是模块1")
    print(__name__)