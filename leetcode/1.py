class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # n = len(nums)
        # lookup = {}
        # for i in range(n):
        #     tmp = target - nums[i]
        #     if tmp in lookup:
        #         return [lookup[tmp], i]
        #     lookup[nums[i]] = i
        n = len(nums)-1
        for i in range(n):
            tmp = target - nums[i]
            if tmp in nums:
                return 

a = Solution().twoSum([2, 7, 11, 15], 9)
print(a)
# print(Solution.twoSum(self,nums =[2, 7, 11, 15],target = 9))