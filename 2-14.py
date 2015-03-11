# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 13:27:51 2015

@author: JK
"""

"""
2-14 完善decorator
"""

import time, functools

def performance(unit):
    def per_decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit == 'ms' else (t2 - t1)
            print 'call %s() in %f %s' % (f.__name__, t, unit)
            return r
        return wrapper
    return per_decorator
            
    
@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
    
print factorial.__name__