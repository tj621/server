'''

@author: Zxh
'''
from scheduler import Scheduler
from indoor import Indoor
from outdoor import Outdoor
from parameter import Parameter
from control import Control
from autorun import auto_run_main
from time import sleep

onode0 = Indoor('node0')
outdoor = Outdoor()
p = Parameter()
c = Control()
control_method = "control"


def auto_running():
    global node0, c, outdoor, p
    auto_run_main(node0, outdoor, c, p)


auto = Scheduler(10, auto_running)


def manul_control():
    global control_method, auto
    if control_method == "auto":
        auto.stop()
    print 'manul_control'
    control_method = "manul_control"


def computer_control():
    global control_method, auto
    if control_method == "auto":
        auto.stop()
    control_method = "computer_control"
    print 'computer control'


def auto_run():
    global control_method, auto
    if control_method == "manul_control" or control_method == "computer_control":
        auto.stop()
    control_method = "auto"
    auto.start()
    return 'auto run'


while 1:
    auto_run()
    sleep(5)
    manul_control()
    sleep(5)
    computer_control()
    