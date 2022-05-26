from datetime import datetime, timedelta

# datetime中的now()函数返回当前日期和时间
today = datetime.now()
print('今天是：' + str(today))

# timedelta()显示一个距今天的时差
one_day = timedelta(days=1)
print(one_day)
one_week = timedelta(weeks=1)
print(one_week)
last_week = today - one_week
print('上个周是：' + str(last_week))
yesterday = today - one_day
print('昨天是：' + str(yesterday))

# .day 存储当前的完整日期的几号 ，是整数;.hour.minute,.second,时,分 ，秒
print('day:' + str(today.day))
print('month:' + str(today.month))
print('year:' + str(today.year))
print('hour:' + str(today.hour))

# datetime.strptime 可以将字符串转化为日期

birthday = input('请输入你的生日（dd/mm/yyyy）')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')  # 大写英文Y代表四个数字
print('我的生日：' + str(birthday_date))
print('我的生日：' + birthday)
