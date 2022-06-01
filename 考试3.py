# books = str([[20,16],[15,11],[10,10],[9,10]])
# books1 = ' '.join(books)
# print(books1)
import idna


N = 6
list1 = list("10 20 30 15 23 12".split())
M = 3

list2 = []
res = 0
a = 0
while M<= N:
    try:
        for i in list1[a:M]:
            res = res +int(i)
        list2.append(res)
        res = 0
        M = M+1
        a = a+1
    except:
        break
print(max(list2))





# while M<N:
#     try:
#         (i = 0
#         while i < M:
#             try:
#                 maxres = int(maxres) + int(list1[i])
#                 i = i+1
#             except:
#                 pass
#     list2.append(maxres)
#     print(list2))
#     except:
#         pass


# print(max(list2))