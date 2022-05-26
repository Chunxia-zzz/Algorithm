# if语句使用要用冒号，然后执行语句前要加四个空格，是缩进，才能使用
price = input('你花了多少钱?')
price = float(price)
if price >= 1.00:
    tax = .07
    print(tax)
else:
    tax = 0
    print(tax)
# 上下两种if语句都可以，注意缩进的位置
if price >= 1.00:
    tax = .07
else:
    tax = 0
print('税率为' + str(tax))

country = 'CANADa'
print(country.lower())  # .lower()是将大写英文转为小写
# 在python中，比较字符串的时候，一个大写，一个小写是不一样的，不能识别相同
