# encoding:UTF-8

"""
装饰器
"""
import time


def run_time(func):
    # @functools.wraps(fun)
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        running_time = end_time - start_time
        print('function running time is {}'.format(running_time))

    return wrapper


@run_time
def func_1():
    time.sleep(1)


test = func_1
print(test)
