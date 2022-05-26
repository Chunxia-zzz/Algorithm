# syntax errors 语法错误，有语法错误代码就完全不会运行

x = 42
y = 206
if x == y:  # 忘记加 ：，即为语法错误 。if要加 : ，下一个语句要空格，不然就是错的
    print('success!')

# runtime errors 运行时错误，代码在运行时出的错误就不能运行了
x1 = 42
y1 = 0
print(x / y)  # 除数不能等于零

# bug是代码中出现的错误，知错不改代码将无法运行

# logic error 逻辑错误，代码运行成功，但会有逻辑错误，不会提示语法错误和运行时错误，只是结果不是我们想要的
a = 204
b = 12
if a < b:  # 比较错误了 ，跟预期结果不一样，我们写代码要仔细
    print(str(a) + '大于' + str(b))

print()
try:
    print(x1 / y1)
except ZeroDivisionError as e:
    print('不能除以0')
else:
    print('其他地方有错误')
finally:
    print('清除代码')
print()
