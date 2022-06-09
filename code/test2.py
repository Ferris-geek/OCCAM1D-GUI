"""

import re


a = "/a/b/c/b/d"
pattern = '/.*/'
p = re.compile(pattern)
path = re.findall(p, a)[0]
edifile = re.split(p, a)[1]
edifile.replace('.edi',"")
print(path, edifile)
"""
import time
import os

timenow = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time()))
print(timenow)
os.system('mkdir ./result/%s'%timenow)