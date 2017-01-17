# coding=utf-8
from threading import Timer


class Scheduler(object):
    def __init__(self, sleep_time, function):
        self.sleep_time = sleep_time
        self.function = function
        self._t = None

    def start(self):
        if self._t is None:
            self._t = Timer(self.sleep_time, self._run)
            self._t.start()
        else:
            raise Exception("this timer is already running")

    def _run(self):
        self.function()
        self._t = Timer(self.sleep_time, self._run)
        self._t.start()

    def stop(self):
        if self._t is not None:
            self._t.cancel()
            del self._t


# test

# def update_indoor():
# print 'indoor updated'
#
#
# def update_outdoor():
#     print 'outdoor updated'
#
#
# def update_control():
#     print 'control updated'
#
# scheduler1 = Scheduler(5, update_outdoor)
# scheduler2 = Scheduler(300, update_indoor)
# scheduler3 = Scheduler(300, update_control)
# scheduler1.start()
# scheduler2.start()
# scheduler3.start()
