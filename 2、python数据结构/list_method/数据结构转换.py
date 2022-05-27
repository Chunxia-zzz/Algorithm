"""
数组(元素为str)转字符串
str = "".join(list)
<需要在每个元素中间添加的字符>’.join(<目标list，且所有元素都为str类型>)

数组(元素为int)转字符串
str = "".join(map(str,list))
重要：使用map方法将数组内的int转换成了str

数组(元素为int)转int

算法题：
1、实现list中的数字组成的数加1，题目是英文的，list形式输出
输入[1,2,3,4] 输出[1,2,3,5]
输入[9,9,9]  输出[1,0,0,0]
思路：转换成int,+1，再把int按位转换成数组
"""

# nums = ['0', '1', '1', '2', 'I', 'a']
# print(nums)

# #使用join方法将数组的值转换成字符串，中间可选分隔符
# res = ''.join(nums)
# print(res)

nums = [0, 1, 1, 2, 6, 88]

res = ''.join(map(str,nums))
print(res)

int1 = int(res)
print(int1 + 1)

str1 = str(int1)
x = []
for i in str1:
    x.append(i)
x = list(map(int,x))
print(x)



# list1 = list(str1.split(" "))
# print(list1)