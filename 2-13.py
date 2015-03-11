# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 12:39:01 2015

@author: JK
"""

"""
2-13 编写带参数decorator
"""

import time

def performance(unit):
    def per_decorator(f):
        def fn(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = t2 - t1
            if unit == 'ms':
                print 'call %s() in %fms' % (f.__name__, t *1000)
            else:
                print 'call %s() in %fs' % (f.__name__, t)
            return r
        return fn
    return per_decorator

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
    
print factorial(10)