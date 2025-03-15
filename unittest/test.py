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


def test1_2():
    """
    以下程序输出结果是
    n= 3
    """
    n = 1
    def func(a):
        n = a

        def func1():
            global n
            n = a + 1

        def func2():
            print('n=', n)

        return func1, func2

    f1, f2 = func(3)
    f1()
    f2()


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
        a = a + [3, 4]  # 重新申请内存, 函数外的a不修改
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
        a = (a,)
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
    True
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

    bar_one = Bar.create_one()
    bar_two = Bar.create_two()
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


def test14():
    """
    s1
    s2
    run
    e2
    e1
    """

    def decorator1(func):
        def wrapper():
            print('s1')
            func()
            print("e1")

        return wrapper

    def decorator2(func):
        def wrapper():
            print('s2')
            func()
            print("e2")

        return wrapper

    @decorator1
    @decorator2
    def show():
        print('run')

    show()


def test15():
    """
    3
    """
    import re

    content = "i think 123 is a lucky num."
    res = re.match(".*(\d+).*", content)
    if res:
        print(res.group(1))


def test16():
    print(f'{{1')
    print(f'{{{1}')


def test17():
    if True: print(1)
    if True:
        print(1)

    # if True:
    # print(1)
    if True:
        print(1)


def test16():
    """
    [0, 1, 2, 3, 4]
    []
    1. 定义__iter__表明类为一个迭代器，只在迭代开始时运行一次
    2. 循环调用 __next__ 直到遇到 raise StopIteration 为止
    """

    class Yrange():
        def __init__(self, n):
            self.i = 0
            self.n = n

        def __iter__(self):
            return self

        def __next__(self):
            if self.i < self.n:
                i = self.i
                self.i += 1
                return i
            else:
                raise StopIteration()

    y = Yrange(5)
    print(list(y))
    print(list(y))


def test17():
    """
    [0, 1, 2, 3, 4]
    [0, 1, 2, 3, 4]
    """
    class Yrange():
        def __init__(self, n):
            self.i = 0
            self.n = n

        def __iter__(self):
            return self

        def __next__(self):
            if self.i < self.n:
                i = self.i
                self.i += 1
                return i
            else:
                raise StopIteration()

    class Zrange:
        def __init__(self, n):
            self.n = n
        def __iter__(self):
            return Yrange(self.n)

    z = Zrange(5)
    print(list(z))
    print(list(z))


def test18():
    """
    0.8382096596190508
    0.07572377720016632
    0.8363375023320742
    0.07572377720016632
    0.8382096596190508
    """
    import random

    random.seed('2021')
    print(random.random())

    for seed, version in (('2021', 1), (2021, 2), (b'2021', 1), (bytearray(b'2021'), 2)):
        random.seed(seed, version=version)
        print(random.random())


def test19():
    """
    False
    False
    """
    import math

    print(math.isfinite(float("inf")))
    print(math.isinf(float("0")))


def test21():
    """
    ['End']
    ['End', 'End']
    ['1', '2', 'End']
    ['End', 'End', 'End']
    """

    class Test(object):
        def process_data(self, data=[]):
            data.sort()
            data.append("End")
            return data

    t1 = Test()
    print(t1.process_data())
    print(t1.process_data())
    t2 = Test()
    print(t2.process_data(data=['1', '2']))
    print(t2.process_data())


def test22():
    """
    TypeError: f() missing 1 required positional argument: 'self'
    """

    class A:
        def f(self):
            print(1)

        @staticmethod
        def f(self):
            print(2)

    a = A()
    print(a.f())


def test23():
    print((2) << 2)  # 8: 0b0010 -> 0b1000
    # 1 + 2j << 2  TypeError: unsupported operand type(s) for <<: 'complex' and 'int'
    # [2] << 2  TypeError: unsupported operand type(s) for <<: 'list' and 'int'
    # 2.0 << 2  TypeError: unsupported operand type(s) for <<: 'float' and 'int'


def test24():
    """4"""

    class Person:
        __slots__ = ('name', 'age')

    class Student(Person):
        pass

    stu = Student()
    stu.name = "Mike"
    stu.age = 10
    stu.grade = 4
    print(stu.grade)


def test25():
    """[5, 4, 1, 2, 3]"""
    from collections import deque

    dq = deque([1])
    dq.extend([2, 3])
    dq.extendleft([4, 5])
    print(list(dq))


def test26():
    """
    (A), A(), A print(0)
    A{} raise
    """
    class A:
        x = 0

    for a in ((A), A(), A):
        print(a.x)

    # a = A{}
    # print(a.x)


def test27():
    """
    {{表示转义{
    {40}
    {4*10}
    40
    4*10
    """
    print(f"{{{4*10}}}")
    print(f"{{4*10}}")
    print(f"{4 * 10}")
    print(f"4*10")


def test28():
    """
    返回列表的地址，没有改变
    True
    [['def'], ['abc']]
    """
    def foo(x):
        x[0] = ['def']
        x[1] = ['abc']
        return id(x)

    q = ['abc', 'def']
    print(id(q) == foo(q))
    print(q)


def test29():
    """
    False
    True
    """
    class Foo:
        def __init__(self, name):
            self._name = name

        def __str__(self):
            return self._name

        def __eq__(self, other):
            return self is other

    class Bar:
        def __init__(self, name):
            self._name = name

        def __str__(self):
            return self._name

        def __eq__(self, other):
            return str(self) == str(other)

    foo = Foo("Hello")
    bar = Bar("Hello")
    print(foo == bar)
    print(bar == foo)


def test30():
    import importlib
    # importlib.import_module("a.a")  # wrong
    # a = importlib.import_module("a")  # wrong
    # from a import a  # ok
    a = importlib.import_module("a.a")  # ok
    a.func


def test31():
    # IndentationError: unexpected indent
    # s = 'a' + 'b'
    #     + 'c' + 'd'
    #     + 'e' + 'f'
    s = 'a' + 'b' \
        + 'c' + 'd' \
        + 'e' + 'f'
    s = ('a' + 'b'
        + 'c' + 'd'
        + 'e' + 'f')
    s = 'a' + 'b' \
        + 'c' + 'd' \
        + 'e' + 'f' \

    1


def test32():
    """
    # from a import func    # 循环引用
    # from a.a import *     # ok
    #                       # 报错
    # from .a import *        # ok
    """
    from a import func
    func()


def test33():
    """
    It is not the same thread.
    It is not the same thread.
    """
    import threading
    import asyncio

    async def hello(thread_id):
        current_thread = threading.current_thread()
        if thread_id == current_thread:
            print('It is not the same thread.')

    async def main():
        main_thread = threading.current_thread()
        hello1 = asyncio.create_task(hello(main_thread))
        await hello(main_thread)
        await hello1

    asyncio.run(main())


def test34():
    """
    3
    2
    1
    """
    import unittest
    import math
    from unittest import mock

    class TestSample(unittest.TestCase):
        @mock.patch.object(math, 'sqrt')
        @mock.patch.object(math, 'ceil')
        @mock.patch.object(math, 'degrees')
        def test_math(self, test_mock_1, test_mock_2, test_mock_3):
            test_mock_1.return_value = 1
            test_mock_2.return_value = 2
            test_mock_3.return_value = 3
            print(math.sqrt(1))
            print(math.ceil(1))
            print(math.degrees(1))


    unittest.main()


def test35():
    """2"""
    y = 1
    f = lambda x: x+ y+ 1
    y = 0
    print(f(1))


def test36():
    """
    True
    False
    """
    import collections

    a = range(10)
    # a = (x for x in range(10))
    print(isinstance(a, collections.Iterable))
    print(isinstance(a, collections.Iterator))