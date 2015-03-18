from __future__ import unicode_literals

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 20:02:48 2015

@author: JK
"""

"""
3-4 使用__future__

在Python 3.x中，字符串统一为unicode，不需要加前缀 u，而以字节存储的str则必须加前缀 b。请利用__future__的unicode_literals在Python 2.7中编写unicode字符串。
"""

s = 'am I an unicode?'
print isinstance(s, unicode)