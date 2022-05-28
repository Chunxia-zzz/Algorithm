a = 'AACTGTGCACGACCTGA'
n = 5
k = n
arr1 = []
i = 0
while i < len(a)- k:
    arr1.append(a[i:n])
    i+=1
    n+=1

arr2 = []
for i in arr1:
    b = i.count('c')+i.count('G')
    arr2.append(b)
print(arr2)

max_value  = max(arr2)
idx = arr2.index(max_value)
print(arr1[idx])