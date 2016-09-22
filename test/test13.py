'''

@author: Zxh
'''
from time import sleep

a = {'hehe': -0.7}
c = 12.0
str = 'hehe'
value = a.get(str)
print value
print abs(value)
print c * abs(value)
if value < 0:
    print 'game'
    sleep(c * abs(value) / 10)
    print 'over'

if __name__ == '__main__':
    print 'test'