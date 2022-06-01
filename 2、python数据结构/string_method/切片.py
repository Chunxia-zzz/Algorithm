'''
输入
abABCcDEF
6
输出：
abABCc

切前n位[0:n]
后len(str)-n位 [n:0]

切后n位[len(str)-n:0]
剩余

print(str1[0:n])
截取字符串，使用思路切片

'''
# while True:
#     try:
#         s=input()           
#         while len(s)>8:               
#             print(s[:8])               
#             s=s[8:]           
#         print(s.ljust(8,"0"))
#     except:
#         break

a = 200
b = bin(a)
c =b[2:].split('0')
print(c)
print(len(max(c)))
