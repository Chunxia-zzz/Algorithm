"""描述
输入一行字符，分别统计出包含英文字母、空格、数字和其它字符的个数。

数据范围：输入的字符串长度满足
1≤n≤1000

输入描述：
输入一行字符串，可以有空格

输出描述：
统计其中英文字符，空格字符，数字字符，其他字符的个数

示例1
输入：
1qazxsw23edcvfr45tgbnhy67ujm, ki89ol.\\ /;p0 -=\\][
复制
输出：
26
3
10
12
"""
# 思路：考了字符串的几个API，对值类型的判断
a = '1qazxsw23 edcvfr45tgbn hy67uj m,ki89ol.\\/;p0-=\\]['
# a = input()
b = 0
c = 0
d = 0
for i in a:
    if i.isalpha():
        b += 1
    elif i == ' ':
        c += 1
    elif i.isnumeric():
        d += 1
print(b)
print(c)
print(d)
print(len(a) - b - c - d)
