#  Mastering Python High Performance
#  http://proquest.safaribooksonline.com.ezproxy.spl.org:2048/book/programming/python/9781783989300/pypy/ch06lvl2sec51_html?uicode=spl

from cStringIO import StringIO
import time

TIMES = 100000

#  Normal Python style string concatenation
init = time.clock()
value = ''
for i in range(TIMES):
    value += str(i)
print("Concatenation: %s" % (time.clock() - init))

#  cStringIO concatenation
init = time.clock()
value = StringIO()
for i in range(TIMES):
    value.write(str(i))
print("StringIO: %s" % (time.clock() - init))

#  List concatenation
init = time.clock()
value = []
for i in range(TIMES):
    value.append(str(i))
finalValue = ''.join(value)
print("List: %s" % (time.clock() - init))
