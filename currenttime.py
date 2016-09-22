import time
import datetime

from scheduler import Scheduler



def get_current_time():
    local_time = time.localtime(time.time())
    return time.strftime("%Y-%m-%d %X", local_time)


# return "2016-16-16 12:21"
def get_current_month():
    local_time = time.localtime(time.time())
    return "%s" % (local_time[1])


def get_current_hour():
    local_time = time.localtime(time.time())
    return "%s" % (local_time[3])


def get_time():
    return time.time()

def make_time(value,if_end):
    if if_end<1:
        value+=' 00:00:00'
    else:
        value += ' 23:56:00'
    return  time.strftime("%Y-%m-%d %X",time.strptime(value, '%Y-%m-%d %X'))

def make_time_stamp(value):
    time_array=time.strptime(value,"%Y-%m-%d %X")
    time_stamp = int(time.mktime(time_array))
    return time_stamp

def stamp_to_time(timeStamp):
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime

def stamp_for_series_start_time(time_value):
    # time_value += ' 00:00:00'
    temp = str(int(make_time_stamp(time_value))+8*3600)
    return temp+'000'

if __name__ == '__main__':
    a="2016-8-23 00:00:00"
    print  stamp_for_series_start_time(a)
    print stamp_to_time(1471910400)
    # print make_time(a,0)
    # print time.time("2016-7-23")
    # print get_current_time()
    # time.sleep(5)
    # print get_current_time()
    # while(1):
    #     time.sleep(5)
    #     print get_current_time()
    # print time.time()
    # print time.localtime(time.time())
    # print get_current_month()
    # print get_current_hour()
    # print get_time()
