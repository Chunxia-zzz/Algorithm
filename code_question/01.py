# encoding:UTF-8

"""
baidu second 2: 
读取某一个文件，按照其中的学号进行排序，然后存到数据库中

知识点：IO文件读写，接收数据，排序，连数据库，sql语句
"""

import numpy as np
import pandas as pd
import pymysql

# step1:读取文件，转换为可操作的数据类型
dataframe = pd.read_excel('D:/VScode Workspace/Algorithm/data/Student.xlsx')
# print(L)
L_array = np.array(dataframe)
L_list = L_array.tolist()


# step2:排序
def by_id(i):
    return i[0]


L_sort = sorted(L_list, key=by_id)
print(L_sort)

# step3:连接数据库，用sql语句写入数据

student_center = pymysql.connect(host='xxxx',
                                 port="int",
                                 user='xxxx',
                                 database='student_center',
                                 passwd='xxxxx')

cursor = student_center.cursor()
for i in L_sort:
    cursor.execute("INSERT INTO `student`(`id`, `name`, `age`) VALUES tuple(i)")
