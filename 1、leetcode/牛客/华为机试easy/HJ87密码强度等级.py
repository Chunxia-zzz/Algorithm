"""
描述
密码按如下规则进行计分，并根据不同的得分为密码进行安全等级划分。

一、密码长度:
5 分: 小于等于4 个字符
10 分: 5 到7 字符
25 分: 大于等于8 个字符

二、字母:
0 分: 没有字母
10 分: 密码里的字母全都是小（大）写字母
20 分: 密码里的字母符合”大小写混合“

三、数字:
0 分: 没有数字
10 分: 1 个数字
20 分: 大于1 个数字

四、符号:
0 分: 没有符号
10 分: 1 个符号
25 分: 大于1 个符号

五、奖励（只能选符合最多的那一种奖励）:
2 分: 字母和数字
3 分: 字母、数字和符号
5 分: 大小写字母、数字和符号

最后的评分标准:
>= 90: 非常安全
>= 80: 安全（Secure）
>= 70: 非常强
>= 60: 强（Strong）
>= 50: 一般（Average）
>= 25: 弱（Weak）
>= 0:  非常弱（Very_Weak）

对应输出为：

VERY_SECURE
SECURE
VERY_STRONG
STRONG
AVERAGE
WEAK
VERY_WEAK

请根据输入的密码字符串，进行安全评定。

注：
字母：a-z, A-Z
数字：0-9
符号包含如下： (ASCII码表可以在UltraEdit的菜单view->ASCII Table查看)
!"#$%&'()*+,-./     (ASCII码：0x21~0x2F)
:;<=>?@             (ASCII码：0x3A~0x40)
[\]^_`              (ASCII码：0x5B~0x60)
{|}~                (ASCII码：0x7B~0x7E)
提示:
1 <= 字符串的长度<= 300
输入描述：
输入一个string的密码

输出描述：
输出密码等级

示例1
输入：
38$@NoNoN
复制
输出：
VERY_SECURE
复制
说明：
样例的密码长度大于等于8个字符，得25分；大小写字母都有所以得20分；有两个数字，所以得20分；包含大于1符号，所以得25分；由于该密码包含大小写字母、数字和符号，所以奖励部分得5分，经统计得该密码的密码强度为25+20+20+25+5=95分。

"""
# 傻逼题目
a = input()
score = 0
if len(a) <= 4:
    score += 5
elif 5 <= len(a) <= 7:
    score += 10
else:
    score += 25

low = 0
up = 0
dig = 0
fuhao = 0
for i in a:
    if i.islower():
        low = 1
    elif i.isupper():
        up = 1
    elif i.isdigit():
        dig += 1
    elif i.isascii():
        fuhao += 1

if dig > 1:
    dig = 2
if fuhao > 1:
    fuhao = 2.5

score += 10 * (low + up + dig + fuhao)
bonus = 0
if low != 0 or up != 0:
    if dig != 0:
        bonus = 2
        if fuhao != 0:
            bonus = 3
            if low != 0 or up != 0:
                bonus = 5
score += bonus

if score >= 90:
    print('VERY_SECURE')
elif score >= 80:
    print('SECURE')
elif score >= 70:
    print('VERY_STRONG')
elif score >= 60:
    print('STRONG')
elif score >= 50:
    print('AVERAGE')
elif score >= 25:
    print('WEAK')
else:
    print('VERY_WEAK')
