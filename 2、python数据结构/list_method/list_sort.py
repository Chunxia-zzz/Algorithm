"""
排序
numbers.sort()

反向排序
numbers.sort(reverse=True)

算法题1：数组从后向前遍历
思路，先反向排序，再for循环遍历
"""
nums = ['Michael', 'Bob', 'Tracy']
print(nums)

# 正向排序
nums.sort()
print(nums)

#反向排序
nums.sort(reverse=True)
print(nums)

#先反向排再for循环，实现数组从后向前遍历
for i in nums:
    print(i)