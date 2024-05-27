"""
描述
找出字符串中第一个只出现一次的字符
1≤n≤1000
输入描述：
输入一个非空字符串

输出描述：
输出第一个只出现一次的字符，如果不存在输出-1

示例1
输入：
asdfasdfo

复制
输出：
o
"""
a = input()
dic = {}
for i in a:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
# print(dic)

nums = [i for i, value in dic.items() if value == 1]
if nums:
    print(nums[0])
else:
    print('-1')
