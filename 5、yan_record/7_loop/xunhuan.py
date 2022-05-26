# 两种循环 for();while()
# name 是一个变量，在in数组中循环，第一次循环值为honghong,第二次循环值为lili,每次自动遍历列表
for name in ['honghong', 'lili']:
    print(name)

# range()会自动为你创建一个整数列表
# 设置循环的次数
for index in range(0, 2):  # (0,2),0是循环开始的位置。2是循环结束的位置
    print(index)

# while()循环 可以指定具体的条件，只要条件为True,会执行while()循环内部的语句
# # 条件一定是可以变动的
names = ['baba', 'mama', 'wo']
index = 0
while index < len(names):
    print(names[index])
    index = index + 1

for na in names:
    print(na)
