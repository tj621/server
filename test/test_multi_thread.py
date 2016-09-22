'''

@author: Zxh
'''
from time import sleep, ctime
import threading

x = 1


def music(value):
    global x
    while x < 40:
        print "I was listening to music. %s" % ctime()
        x += 1
        sleep(1)
        print x
        print value


def move(value):
    global x, t2
    print value
    while x != 30:
        t2.stop()


if __name__ == '__main__':
    global t2
    t2 = threading.Thread(target=music, args=("hehe"))
    t1 = threading.Thread(target=move, args=("dsw"))
    t1.start()
    t2.start()
    print "all over %s" % ctime()
    
    