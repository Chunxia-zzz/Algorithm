first_name = 'chaancer'
last_name = 'young'
print(first_name.capitalize() + ' ' + last_name.capitalize())
output1 = 'hello,' + first_name + ' ' + last_name
output2 = 'hello,{} {}'.format(first_name, last_name)  # format的意思是将两个字符串或者变量进行拼接
output3 = 'hello,{0} {1}'.format(first_name, last_name)
output4 = f'hello,{first_name} {last_name}'  # f=format
print(output1)
print(output2)
print(output3)
print(output4)
