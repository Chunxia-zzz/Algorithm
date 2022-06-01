# encoding:UTF-8

"""
赋值： 将一个对象的地址赋值给一个变量，让变量指向该地址
修改不可变对象（str、tuple）需要开辟新的空间
修改可变对象（list等）不需要开辟新的空间

浅拷贝：浅拷贝就是对引用的拷贝

深拷贝：深拷贝就是对对象的资源的拷贝

"""
import copy

# 赋值
# A = "hello"
# print(id(A))
# A = "hello,world"
# print(id(A))
#
# B = [1]
# print(id(B))
# B.append("hello")
# print(B)
# print(id(B))

# 浅拷贝
# a = ['hello', [1, 2, 3]]
# b = copy.copy(a)
# print([id(x) for x in a])
# print([id(x) for x in b])
#
# a[0] = 'world'
# a[1].append(4)
# print(a)
# print([id(x) for x in a])
# print(b)
# print([id(x) for x in b])

# 深拷贝
a = ['hello', [1, 2, 3]]
b = copy.deepcopy(a)
print([id(x) for x in a])
print([id(x) for x in b])

a[0] = 'world'
a[1].append(4)
print(a)
print(b)
print([id(x) for x in a])
print([id(x) for x in b])
