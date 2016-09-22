'''

@author: Zxh
'''
import pickle

j = [1, 2, 3]
k = j
print k is j
x = pickle.dumps(k)
print x
y = pickle.loads(x)
print y
print y == k
print y is k
print y is j
print k is j
