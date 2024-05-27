# encoding:UTF-8

"""
快速排序
1、挑选基准值
2、分割
3、递归排序子序列
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
