"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

"""


# 斐波那契数列：递归。时间复杂度o(2^n)
# def climb(n: int) -> int:
#     if n == 1 or n == 0:
#         return 1
#     return climb(n - 1) + climb(n - 2)


# 循环，自底向上迭代。时间复杂度o(n),空间复杂度o(1)
# def climb(n: int) -> int:
#     i, j, k = 0, 1, 0
#     while k < n:
#         i, j = j, i + j
#         k = k + 1
#     return j


# 记忆化递归，自顶向下
# def climbStairs(self, n: int) -> int:
#     def dfs(i: int, memo) -> int:
#         if i == 0 or i == 1:
#             return 1
#         if memo[i] == -1:
#             memo[i] = dfs(i - 1, memo) + dfs(i - 2, memo)
#         return memo[i]
#
#     # memo: [-1] * (n - 1)
#     # -1 表示没有计算过，最大索引为 n，因此数组大小需要 n + 1
#     return dfs(n, [-1] * (n + 1))


# 自底向上dp。n是正整数，但是真实斐波那契数列是从0开始，所以需要数组长度为n+1
def climb(n: int) -> int:
    dp = [0] * (n + 1)
    dp[1] = dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[-1]


print(climb(10))
