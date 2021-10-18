"""
baidu second 2: 
读取某一个文件，按照其中的学号进行排序，然后存到数据库中

知识点：IO文件读写，接收数据，排序，连数据库，sql语句
"""

# with open('D:/VScode Workspace/Algorithm/data/test.txt', 'r') as f:
#     print(f.readlines())
f = open('D:/VScode Workspace/Algorithm/data/test.txt', 'r')
for line in f.readlines():
    print(line.strip())
id_list = f.readlines()
print(id_list)
