"""
基本数据结构,6种
可变对象：list,dict,set
不可变对象：str,int/float,tuple

定义变量：创建一块内存空间，将值放进去
可变是指：数据结构的值改变，无需申请新的内存空间
不可变是指：数据结构的值改变，要申请新内存空间
"""
String = "字符串" 
print(id(String))
String1 = "字符串" 
print(id(String1))
String = "字符串update" 
print(id(String))

