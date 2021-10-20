# encoding:UTF-8

"""
1、挑选基准值
2、分割
3、递归排序子序列
"""


def quickSort(array):
    left = 0
    right = len(array) - 1

    pivot = array[left]  # 以第一个元素为pivot

    while left < right:
        while left < right and array[right] >= pivot:
            j = j - 1
        array[]
