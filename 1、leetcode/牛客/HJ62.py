"""
描述
输入一个正整数，计算它在二进制下的1的个数。
注意多组输入输出！！！！！！

数据范围：
输入描述：
输入一个整数

输出描述：
计算整数二进制中1的个数
"""
# 用while循环保证多组输出情况，高级函数梭哈了
while True:
    try:
        a = int(input())
        print(bin(a).count('1'))
    except:
        break
