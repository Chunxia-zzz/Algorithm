# 可以给函数创建多个参数
def get_initial(name, force_uppercase):
    if force_uppercase:  # 如果force_uppercase为真，就执行下面的语句
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial


first_name = input('enter your first name：')
first_name_initial = get_initial(first_name, False)  # 给参数传值，按照参数名字依次传值
print('your initial are :' + first_name_initial)


# 可以给参数设置默认值，即当没有给参数传值时，参数取默认值
def get_initial(name, force_uppercase=True):  # 默认值为真
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial


first_name = input('enter your first name：')
first_name_initial = get_initial(first_name)  # 没有给force_uppercase参数传值，那么就会认为是默认值
print('your initial are :' + first_name_initial)

first_name_initial = get_initial(first_name, False)  ##位置表示法传值
first_name_initial = get_initial(force_uppercase=False, \
                                 name=first_name)  # 命名表示法传值，可以不考虑顺序，也使代码更易懂
