def test1():
    """
    以下程序输出结果是
    n= 3
    n= 5
    """
    def func(a):
        n = a

        def func1():
            print('n=', n)

        def func2():
            nonlocal n
            n = a + 2

        return func1, func2

    f1, f2 = func(3)
    f1()
    f2()
    f1()


def test2():
    """
    [1, 2, 3, 4] []
    reversed()返回一个iterator, 一次sorted后为空
    """
    nums = [4, 1, 3, 2]
    rev = reversed(nums)
    print(sorted(rev), sorted(rev))


def test3():
    """4"""
    from threading import Thread

    nums = 1

    def work1():
        global nums
        nums += 1

    def work2():
        global nums
        nums += 2
        print(nums)

    t1 = Thread(target=work1)
    t2 = Thread(target=work2)
    t1.start()
    t1.join()
    t2.start()
    t2.join()


def test4():
    """
    [1, 2, 3, 4]
    [1, 2]
    """
    def fun(a):
        a = a + [3, 4]    # 重新申请内存, 函数外的a不修改
        # a += [3, 4]         # 原位修改，函数外的a一起修改
        print(a)

    a = [1, 2]
    fun(a)
    print(a)


def test5():
    """
    (('string',),)
    ((('string',),),)
    若为set会raise
    """
    a = ("string",)
    for i in range(2):
        a = (a, )
        print(a)


def test6():
    """
    Low
    try无异常时走else, 返回最后的return
    :return:
    """
    def estiamte_data_plane(version):
        try:
            if version.lower() == "true":
                return "High"
        except Exception:
            pass
        else:
            return "Medium"
        finally:
            return "Low"

    print(estiamte_data_plane(True))


def test7():
    import re

    sentence = "we are humans"
    matched = re.match(r"(.*) (.*) (.*)", sentence)
    print(matched.groups())  # ('we', 'are', 'humans')
    print(matched.group())  # we are humans


def test8():
    class Foo:
        def __init__(self, val):
            self._val = val

        def __call__(self, b):
            return self._val * b

        def __add__(self, other):
            return Foo(self._val + int(other))

        def __int__(self):
            return self._val

    foo = Foo(1)
    bar = Foo(2)
    print(foo(3))  # 3
    foo = foo + bar
    print(foo(1))  # 3


def test9():
    """
    3 None
    yield 没有返回值
    """
    def func(x):
        x = yield x
        x = yield x

    m = func(3)
    for x in m:
        print(x, end=' ')


def test10():
    """
    (0, 1, 2)
    """
    def func():
        yield (x for x in range(3))

    for x in func():
        print(tuple(x))


def test11():
    """
    4 12
    """
    x = 12

    def f1(a, b=x):
        print(a, b)

    x = 15
    f1(4)


def test12():
    """
    False
    False
    """
    class Foo:
        @classmethod
        def create_one(cls):
            return cls()

        @staticmethod
        def create_two():
            return Foo()

    class Bar(Foo):
        pass

    bar_one = Bar.create_one
    bar_two = Bar.create_two
    print(isinstance(bar_one, Bar))
    print(isinstance(bar_two, Bar))


def test12():
    """
    [11, 22, 0, 1, 2, 3]
    进程间资源独立
    """
    from multiprocessing import Process

    nums = [11, 22]

    def work1():
        for i in range(4):
            nums.append(i)

    def work2():
        for i in range(4):
            nums.append(i)
        print(nums)

    if __name__ == '__main__':
        t1 = Process(target=work1)
        t2 = Process(target=work2)
        t1.start()
        t1.join()
        t2.start()
        t2.join()

def test13():
    print(not True or 0)  # 0


8/14
