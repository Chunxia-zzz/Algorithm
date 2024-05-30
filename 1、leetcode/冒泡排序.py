"""
思路：通过两层循环遍历所有数字，并比较相邻两个数字的大小，
如果前一个数字大于后一个数字，则交换它们的位置。经过一轮
比较后，最大的数字会被交换到末尾。重复上述过程，直到所有
数字都按照从小到大的顺序排列。
"""


def sort(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

    return nums


if __name__ == '__main__':
    arr = [10, 7, 8, 9, 1, 5]
    print(sort(arr))
