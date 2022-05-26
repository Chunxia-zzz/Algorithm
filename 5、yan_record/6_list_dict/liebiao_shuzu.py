from array import array

names = ['红红', '明明']
print(names)
print(len(names))  # len() 可以抓取数组的长度
names.insert(0, '丽丽')  # insert() 可以在数组的指定位置放东西
print(names)
names.sort()  # 数组自动按照字母表排序
print(names)
presenters = names[0:2]  # [0:2] 是获取数组中的部分值，0指从开头开始，2指 获取两个值
print(presenters)

names = ['xiaohong' 'xiaoming']
print(names)

scores = []  # 空列表
# append()函数，可以向列表里添加值
scores = array('d')  # 声明需要使用的数组类型，d代表数字类型数组
scores.append(98)
scores.append(99)
print(scores)
# 可以通过索引的方式访问列表里的单独项
print(scores[1])  # 索引是从第0项开始的，所有计数都是从0开始，0是第一项，1说第二项

# scores = array('d') #声明需要使用的数组类型，d代表数字类型数组


# 字典的关键是 键值对，，键是first,值为Christopher; 另一对 ，键为last,值为Harrison
person = {}
person = {'first': 'christopher'}
person['last'] = 'Harrison'
print(person)
print(person['first'])
# 输出指定的键的值,字典可以在不知道第几项，通过键找到值

ll = []
ll = [names, person]
print(ll)
