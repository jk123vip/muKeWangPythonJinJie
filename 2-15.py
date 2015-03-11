# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 14:24:55 2015

@author: JK
"""

"""
2-15 偏函数

在第7节中，我们在sorted这个高阶函数中传入
自定义排序函数就可以实现忽略大小写排序。
请用functools.partial把这个复杂调用变成
一个简单的函数：

sorted_ignore_case(iterable)
"""

import functools

sorted_ignore_case = functools.partial(sorted, cmp=lambda s1,s2: cmp(s1.upper(), s2.upper()))

print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])