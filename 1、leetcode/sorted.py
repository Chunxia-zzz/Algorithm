# encoding:UTF-8
# 高级函数的排序方法
# nums.sort()
# 以及下面的sorted

id_list = ['471208', '471648', '471244', '-471158', '-471482', '471333', '471399', '471675', '471626', '471453']
# print(sorted(id_list))

L = [(3, 'Bob', 75), (5, 'Adam', 92), (2, 'Bart', 66), (1, 'Lisa', 88)]


def by_id(i):
    return i[0]


L2 = sorted(L, key=by_id)
print(L2)
