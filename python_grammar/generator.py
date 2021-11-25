# encoding:UTF-8

"""
生成器:也是一个可迭代对象（Iterable），可以直接使用for循环
一边循环一边计算的机制
"""
L = [x * x for x in range(10)]
# print(L)
g = (x * x for x in range(10))
# print(type(g))

#斐波那契数列（Fibonacci）
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(10)

