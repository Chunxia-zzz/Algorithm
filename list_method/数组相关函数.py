"""
sorted(str)方法输出的是数组

.join(x) ’
<需要在每个元素中间添加的字符>’.join(<目标list，且所有元素都为str类型>), 返回一个新的字符串
"""
str1 = "Ihave1nose2hands10fingers"
a = sorted(str1)
print(a)
print("".join(a))