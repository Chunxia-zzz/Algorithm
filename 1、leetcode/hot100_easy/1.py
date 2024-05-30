"""
两数之和
思路：
1、暴力求解 两层for循环，超时
2、哈希表 



给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

 

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]
 

提示：

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案
进阶：你可以想出一个时间复杂度小于 O(n2) 的算法吗？
"""


# 哈希表存储
# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，
# 一般用在 for 循环当中。
class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        lookup = {}
        # 使用enumerate函数来遍历输入数组的索引和值
        for i, value in enumerate(nums):
            if target - value in lookup:
                return [lookup[target - value], i]
            else:
                # value作字典key,nums下标作字典value
                lookup[value] = i


if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))
