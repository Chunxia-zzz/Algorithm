'''
输入
abABCcDEF
6
输出：
abABCc

print(str1[0:n])
截取字符串，使用思路切片
'''
while True:
    try:
        s=input()           
        while len(s)>8:               
            print(s[:8])               
            s=s[8:]           
        print(s.ljust(8,"0"))
    except:
        break
