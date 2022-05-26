# 虚拟环境只是一个文件夹，内含运行程序所需要的所有代码
# 我所做的是将一切安装到这个文件夹，然后就可以使用它
# 首先，我们需要创建这个文件夹，可以用名为virtualenv的工具来实现


pip
install
virtualenv

# 此语句是在终端输入的
python - m
venv < folder_name >  # folder_name 为创建文件夹的名称
# -m 代表特定模块，venv是虚拟环境的缩写，然后具体要创建的目标名称


virtualenv < folder_name >
# 只需要指定创建文件夹的名称

# 当我要使用虚拟环境时，首先要激活它
< folder_name >\Scripts\Activate.bat
# 当用windows系统时，只需要将其放在Scripts目录下就可以激活
.\venv\Scripts\activate.psy
# .\是当前目录
