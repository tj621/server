'''

@author: Zxh
'''

str1 = "01 01 00 00 61 9C"
x = ''.join(str1.split())
hehe = {"s": -1}
if hehe.get("s") < 0:
    print hehe.get("s")
    print abs(hehe.get("s"))

print x
print x[0]
print x[1]
print x[0:2]
print x[4:6]
a = '{0:b}'.format(int(x[4:6], 16))
print a
print len(str(a))
if len(str(a)) < 8:
    str2 = '0'
    for i in range(8 - len(str(a))):
        str2 += '0'
    print str2 + str(a)
print bin(int(x[4:6], 16))