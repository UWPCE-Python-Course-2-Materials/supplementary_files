#  Mastering Python High Performance
#  http://proquest.safaribooksonline.com.ezproxy.spl.org:2048/book/programming/python/9781783989300/pypy/ch06lvl2sec51_html?uicode=spl

import math
import time

TIMES = 100000000

#  Without using a function

init = time.clock()

for i in range(TIMES):
    value = math.sqrt(i * math.fabs(math.sin(i - math.cos(i))))

print("No function: %s" % (time.clock() - init))


#  Factoring the math into a function

def calcMath(i):
    return math.sqrt(i * math.fabs(math.sin(i - math.cos(i))))

init = time.clock()

for i in range(TIMES):
    value = calcMath(i)

print("Function: %s" % (time.clock() - init))
