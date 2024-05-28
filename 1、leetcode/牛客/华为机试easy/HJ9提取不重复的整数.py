"""
描述
输入一个 int 型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
保证输入的整数最后一位不是 0 。

数据范围：
1≤n≤10
输入描述：
输入一个int型整数

输出描述：
按照从右向左的阅读顺序，返回一个不含重复数字的新的整数
示例1
输入：
9876673
输出：
37689

"""
# 思路 注意sort方法可以按照key排序
a = input()[::-1]
lookup = [i for i in a]
lookup2 = list(set(lookup))
lookup2.sort(key=lookup.index)
print(''.join(lookup2))
