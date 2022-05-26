province = input('请输入省份：')
tax = 0
# elif（） province 只能等于一个值，允许设置默认操作(允许使用else)
#  \ 连接下一行代码

if province == 'alberta' \
        or province == 'abcle':
    tax = .05
elif province == 'nunavut':
    tax = .05
elif province == 'ontatio':
    tax = 0.13
else:
    tax = 0.15
print(tax)
# or操作符，或者,
# in操作符  选择其中的任意一个值，使语句更简洁

country = input('你来自哪个国家？')

if country.lower() == 'china':
    province = input('你来自哪个省份？')
    if province in ('shandong', \
                    'guangdong', 'fujian'):
        tax = 0.05
    elif province == 'shanxi' or 'guangxi':
        tax = .13
    else:
        tax = .15
else:
    tax = 0.13

print(tax)
