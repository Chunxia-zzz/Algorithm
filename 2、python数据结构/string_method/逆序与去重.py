'''
字符串逆序直接使用str[::-1]
'''

#句子逆序
str1 = 'I am a boy'
list1 = str1.split()
print(list1)
res = ''
for i in list1:
    res = i+" "+res
    
print(res)

#去重
# res = ''
# for i in str2:
#     if i not in res:
#         res = res + i
# print(res)