m = 3
list1 = [x for x in range(1, 101)]
a = len(list1)

# if m<=1 or m>=100:
#     print("ERROR!")
# else:
# i = m 
# while a >m and i <100:
#     list1.remove(i)
#     i = i + m
#     a = len(list1)
#     # print(a)
#     # print(list1)
i = m - 1
while a > m and i < a - 1:
    list1.remove(list1[i])
    i = i + m - 1
    a = a - 1
    # print(a)
    # print(list1)
if a > m:
    print(list1)
