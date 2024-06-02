"""
描述
根据输入的日期，计算是这一年的第几天。
保证年份为4位数且日期合法。
进阶：时间复杂
输入描述：
输入一行，每行空格分割，分别是年，月，日

输出描述：
输出是这一年的第几天
"""
a = input()
b = list(map(int, a.split(' ')))
sum = b[2]

for i in range(2, b[1] + 1):
    if i == 3:
        if b[0] % 4 == 0 and b[0] % 100 != 0:
            sum += 29
        else:
            sum += 28
    elif i in [2, 4, 6, 8, 9, 11]:
        sum += 31
    else:
        sum += 30

print(sum)
