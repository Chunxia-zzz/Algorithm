"""
"""
import time

class LogTime:
    # def __init__(self, use_int):
    #     self.use_int = use_int
    def __call__(self, func):
        def _log():
            beg = time.time()
            res = func()
            print('use time: {}'.format(time.time()-beg))
            # if self.use_int:
            #     print('use time: {}'.format(time.time()-beg))
            # else:
            #     print('use time: {}'.format(time.time()-beg))
            return res
        return _log 

@LogTime()
def mysleep2():
    time.sleep(2)

mysleep2()
# for i in range(5):
#     print(i)





