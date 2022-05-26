# 模块是有很多函数，类，组建的python文件
# 使用模块可以将代码分解为可重用结构，可让代码更易读
# 创建一个helpers.py  
def display(message, is_warning=False):
    if is_warning:
        print('warning')
    print(message)


# 首先要导入 模块,helpers,是我们创建python脚本的名字
import helpers  # 导入helpers

helpers.display('not a warning')  # 调用helpers中的display()函数，需要先导入helpers,再写函数的名字

# 不想总写 helpers,所以可以用到from语句
from helpers import *  # import * 想从helpers中导入所有，是*的含义

# 一旦导入所有，模块中的所有东西就可以全局获取，
display('not a warning')  # 使用模块中的display(),可以直接写

# 导入模块中的具体项，有助于清除当前的命名空间（helpers）
from helpers import display  # 导入模块中的display(),书写也可以不加helpers前缀

display('not a warning')

# 包 是已经发布的模块集合，可以在网上搜 包
# pip是你会用到的命令行安装程序
pip
install
colorama
# colorama是一个包，打印时改变文本颜色
# 通过pip install指令安装包，然后是包的名字，当完成调用时，会在全局范围内安装该包

# 如果你有一个所有包的列表，你想要安装，可以将其写在文本文件中，经常叫作requirements.txt,可以显示你用的所有包的列表
