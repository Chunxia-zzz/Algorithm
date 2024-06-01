"""
描述
请计算n*m的棋盘格子（n为横向的格子数，m为竖向的格子数）从棋盘左上角出发沿着边缘线从左上角走到右下角，总共有多少种走法，要求不能走回头路，即：只能往右和往下走，不能往左和往上走。
注：沿棋盘格之间的边缘线行走
1≤n,m≤8
输入描述：
输入两个正整数n和m，用空格隔开。(1≤n,m≤8)
输出描述：
输出一行结果
示例1
输入：
2 2
复制
输出：
6
"""


def methods(n, m):
    if n == 0 or m == 0:
        return 1
    if n == 1 and m == 1:
        return 2
    if (n == 2 and m == 1) or (n == 1 and m == 2):
        return 3
    else:
        return methods(n - 1, m) + methods(n, m - 1)


while True:

    try:
        n, m = map(int, input().split())
        result = methods(n, m)
        print(result)
    except:
        break
