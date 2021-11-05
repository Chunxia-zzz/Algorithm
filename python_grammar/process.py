# import multiprocessing
# import time
#
#
# # 多进程编程
# def get_html(n):
#     time.sleep(n)
#     print("sub_progress success")
#     return n
#
#
# if __name__ == "__main__":
#     # 下面这行代码也可以使用继承 multiprocessing.Process 方式实现，就像继承 Thread 方式实现多线程一样
#     progress = multiprocessing.Process(target=get_html, args=(2,))
#     # 打印 pid
#     print(progress.pid)
#     progress.start()
#     print(progress.pid)
#     progress.join()
#     print("main progress end")
