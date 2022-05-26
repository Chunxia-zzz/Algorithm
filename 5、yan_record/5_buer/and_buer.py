lowest_grade = input('请输入你的成绩：')
gpa = input('请输入你的绩点：')
# gpa = float(input('请输入你的绩点：'))  这样的话 gpa就是小数型
if float(gpa) >= 0.85:
    if float(lowest_grade) >= 0.70:
        print('优等生')

# 可以用and连接两个条件,全部符合，两个条件为真 ，结果才为真

if float(gpa) >= 0.85 and float(lowest_grade) >= .70:
    print('优等生')

# 布尔标志 来标记其他地方的if语句， 避免重复使用if语句导致出错，或者为了可读性
# True False 是python中的关键字
# 布尔标志的值 不是 True就是False
if float(gpa) >= 0.85 and float(lowest_grade) >= .70:
    honour_roll = True
else:
    honour_roll = False
if honour_roll:  # 等于 if honour_roll == True:
    print('优等生')
