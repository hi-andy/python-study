def func(x, y=0, z=0):
    print(x)
    print(y)
    print(z)


# 传递可变参数, 接受位置参数
def func2(x, *args):
    print(x)
    print(args)


# 把N个关键字参数，转换成字典的方式
def func3(name, age=18, **kwargs):
    print(name)
    print(age)
    print(kwargs)


def func4(name, age=18, *args, **kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)


# 位置传参
func(5, 6)
# 关键字传参，与参数顺序无关。不能写位置传参之前
# 错误的：func(3, y=5, 7)
func(3, z=2)

func2(1, 2, 3, 4, 5, 6)
func2(*[7, 8, 9, 10])

func3('yonghua', 25, mname='hua', mage=25)
func4('yonghua', 25, 7, 8, 9, mname='hua', mage=25)
func3(**{'name': 'hua', 'age': 25})
