import functools
import time


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        t = time.time()
        result = fn(*args, **kw)
        print('%s executed in %s ms' % (fn.__name__, time.time() - t))
        return result

    return wrapper
