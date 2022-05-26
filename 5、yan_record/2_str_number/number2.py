day_in_feb = 28
print(str(day_in_feb) + ' days in February')  # str()字符串转化，将数字转换成字符串
a = '6'
b = '5'  # 加上引号 a,b就变成了字符串 5和6，不能进行数字加减
print(a + b)
first_num = input('enter first number：')
second_num = input('enter second number：')
print(first_num + second_num)  # 让用户输入的数字也会默认为字符串，用加号只能做拼接
# int()函数 是将字符串转化成整数
# float()函数 是将字符串转为 带小数点的浮点数
# 使用数字相加时，确保类型相同
# modul()是需要在数组和列表中指定索引值
print(int(first_num) + int(second_num))
print(float(first_num) + float(second_num))
