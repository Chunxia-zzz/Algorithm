"""
索引，索引取值
"""
list1 = [1, 1, 2, 2, 2, 1, 2, 1, 1, 1, 1, 1]
max_value  = max(list1)
idx = list1.index(max_value)
print(idx)

x = list(enumerate(list1))
print(x)

list2 = [0,1,2]
#-1表示最后一位，-2表示倒数第二位。依此类推
print(list2[-1])