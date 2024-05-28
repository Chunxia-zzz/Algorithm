"""
输入描述：
先输入键值对的个数n（1 <= n <= 500）
接下来n行每行输入成对的index和value值，以空格隔开

输出描述：
输出合并后的键值对（多行）
输入：
4
0 1
0 2
1 2
3 4
输出：
0 3
1 2
3 4
"""
a = int(input())
b = {}
while a > 0:
    i = input()
    j = list(i.split(' '))
    if j[0] not in b:
        b[j[0]] = j[1]
    else:
        b[j[0]] = int(b[j[0]]) + int(j[1])
    a = a - 1

for key in sorted(b):
    print(key, b[key])
