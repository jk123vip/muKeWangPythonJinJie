# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 19:42:31 2015

@author: JK
"""

"""
3-2 导入模块

Python的os.path模块提供了 isdir() 和 isfile()函数，请导入该模块，并调用函数判断指定的目录和文件是否存在。

注意: 

1. 由于运行环境是平台服务器，所以测试的也是服务器中的文件夹和文件，该服务器上有/data/webroot/resource/python文件夹和/data/webroot/resource/python/test.txt文件，大家可以测试下。

2. 当然，大家可以在本机上测试是否存在相应的文件夹和文件。
"""

from os.path import isdir, isfile

print isdir(r'/data/webroot/resource/python')
print isfile(r'/data/webroot/resource/python/test.txt')