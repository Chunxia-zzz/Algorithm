# -*- coding: utf-8 -*-

"""
列表生成式：List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
写列表生成式时，把要生成的元素x放到前面，后面跟for循环，就可以把list创建出来，for循环后面还可以加上if判断，这样我们就可以筛选。
"""

exp = [m + n for m in 'ABC' for n in 'XYZ']
print(exp)
# ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']


L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]


# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
