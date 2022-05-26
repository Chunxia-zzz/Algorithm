# def 定义一个函数。 print_time(),函数要加括号，print_time,为函数名

from datetime import datetime


def print_time():
    print('task comleted')
    print(datetime.now())
    print()


first_name = 'susan'
print_time()
for x in range(0, 10):
    print(x)
print_time()  # 直接调用函数


# 使用函数，可以是使代码更易懂，调用函数可以让整体看起来很整洁，减少重复代码的书写
# 定义函数时，可以先给函数一个参数，但是调用时 就要给参数一个值

def yy(task_name):
    print(task_name)  # 使用参数可以执行不同任务时有不同的信息
    print(datetime.now())
    print()


first_name = 'susan'
yy('first name assigned')  # 调用时给参数一个值
for x in range(0, 10):
    print(x)
yy('loop complioted')

first_name = input('输入你的第一个名字：')
first_name_initial = first_name[0:1]  # [0：1]获取首字母
last_name = input('输入你最后一个名字：')
last_name_initial = last_name[0:1]
print('Your initials are:' + first_name_initial + last_name_initial)

print()


# 用函数执行上面的语句
# 使用函数时，记得注释函数的作用，使用参数时，记得注释参数的作用，这样以后浏览时更易懂
def get_initial(name):
    initial = name[0:1].upper()  # upper(),转化为大写，在函数中，需要改动，只要改动一个地方就可以啦
    return initial  # 返回函数的一个值


first_name1 = input('请输入你的第一名字：')
first_name_initial1 = get_initial(first_name1)  # 调用函数get_initial(),并将返回值存储在first_name_initial1中
last_name1 = input('请输入最后一个名字：')
last_name_initial1 = get_initial(last_name1)

print('Your initials are:' + first_name_initial1 + last_name_initial1)

print()


# 简单的书写方式
def get_initial(name):
    initial = name[0:1].upper()  # upper(),转化为大写，在函数中，需要改动，只要改动一个地方就可以啦
    return initial  # 返回函数的一个值


first_name2 = input('请输入你的第一名字：')
last_name2 = input('请输入最后一个名字：')

print('Your initials are:' + \
      get_initial(first_name2) + \
      get_initial(last_name2))
