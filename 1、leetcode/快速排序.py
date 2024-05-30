# encoding:UTF-8

"""
这段代码首先检查输入数组的长度，如果长度小于等于1，则直接返回数组（因为它已经是排序好的）。
接着，选择数组中的第一个元素作为基准值（pivot），
然后创建两个列表：一个用于存放比基准值小的元素，另一个存放比基准值大的元素。
之后，递归地对这两个列表进行快速排序，并将排序后的结果与基准值连接起来，从而得到完整的排序数组。
这是一种非原地排序实现，因为它产生了额外的列表。对于大量数据排序，可能会有较高的内存消耗。
"""


def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        pivot = nums[0]
        left = [i for i in nums[1:] if i <= pivot]
        right = [i for i in nums[1:] if i > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == '__main__':
    arr = [10, 7, 8, 9, 1, 5]
    print(quick_sort(arr))

# 想办法理清
# def quickSort(array):
#     left = 0
#     right = len(array) - 1
#
#     pivot = array[left]  # 以第一个元素为pivot
#
#     while left < right:
#         while left < right and array[right] >= pivot:
#             j = j - 1
#         array[]
