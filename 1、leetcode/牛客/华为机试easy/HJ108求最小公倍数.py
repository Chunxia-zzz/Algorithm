"""
描述
正整数A和正整数B 的最小公倍数是指 能被A和B整除的最小的正整数值，设计一个算法，求输入A和B的最小公倍数。

数据范围：
1≤a,b≤100000
输入描述：
输入两个正整数A和B。

输出描述：
输出A和B的最小公倍数。
示例1
输入：
5 7
输出：
35
示例2
输入：
2 4
输出：
4
"""
# 这里利用了a*b=他们的最大公约数*最小公倍数

import math

a, b = map(int, input().split())
# for i in range(max(a,b), a*b+1, max(a,b)):
#     if i % min(a,b) == 0:
#         print(i)
#         break
print(a * b // math.gcd(a, b))
