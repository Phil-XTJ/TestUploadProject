class cla:
    def __init__(self,value):
        print("我被实例化了，数值为：%d" %value)
    def tt(self):
        print("我是一个类对象")

def test1():
    print("test1")

def test2():
    print("te2\n2st")

def test3():
    print("test3")

if __name__ == "__main__":   #防止主文件调用模块文件时也执行如下代码
    test1()
    test2()
    test3()

