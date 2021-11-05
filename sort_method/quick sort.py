# encoding:UTF-8

"""
1、挑选基准值
2、分割
3、递归排序子序列
"""
# encoding:UTF-8


def partition(arr, low, high):
    i = (low - 1)  # 最小元素索引
    pivot = arr[high]

    for j in range(low, high):

        # 当前元素小于或等于 pivot
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)



def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


if __name__ == '__main__':
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quickSort(arr, 0, n - 1)
    print("排序后的数组:")
    for i in range(n):
        print("%d" % arr[i])

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
