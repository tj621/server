'''

@author: Zxh
'''

from outdoor import Outdoor
from control import Control
from indoor import Indoor
from parameter import Parameter
from currenttime import get_current_hour, get_current_month, get_current_time, get_time


class Ghauto:
    def heating(self, Indoor, Parameter, Control):
        if Indoor.get_temperature() < Parameter.hearting_start_lowest_temperature:
            Control.set_heating("on")
        elif Indoor.get_temperature() > Parameter.hearting_stop_highest_temperature:
            Control.set_heating("off")

    def fogging(self, Indoor, Parameter, Control):
        if Indoor.get_temperature() > Parameter.temperature_to_open_fogging + 1:
            Control.set_fogging("on")
            # if Control.get_thermal_screen()=="on"
            # Control.set_thermal_screen("off")
        elif Indoor.get_temperature() < Parameter.temperature_to_open_fogging - 1:
            Control.set_fogging("off")

    def cooling_pump(self, Indoor, Parameter, Control):
        if Indoor.get_temperature() > (Parameter.temperature_to_open_cooling_pad + 1):
            Control.set_cooling_pad("on")
        elif Indoor.get_temperature() < (
            Parameter.temperature_to_open_cooling_pad - 1):  # 此时侧窗是与湿帘风机对应的，所以暂时不需要考虑90度方向的侧窗是否关闭
            Control.set_cooling_pad("off")

    def co2(self, Indoor, Parameter, Control):
        if Indoor.get_co2() < Parameter.co2_lower_limit:
            Control.set_co2("on")
        elif Indoor.get_co2() > Parameter.co2_upper_limit:
            Control.set_co2("off")

    def irrigation(self, Indoor, Parameter, Control):
        pass


    open_time = 0
    open_time2 = 0
    stop_time = 0
    stop_time2 = 0
    stop_time3 = 0

    def lighting(self, Outdorr, Parameter, Control):  # 补光策略，在currenttime 加了一个get_time()函数

        while True:
            if Control.get_lighting_1() == "off" and Control.get_lighting_2() == "off":
                if get_current_month() > Parameter.month_to_open_lighting and get_current_month() < Parameter.month_to_close_lighting:
                    if get_current_time() > Parameter.period1_start_lighting and get_current_time() < Parameter.period1_stop_lighting:
                        if Outdoor.radiation < Parameter.radiation1_to_open_lighting:
                            Control.set_lighting_1("on")
                            open_time = get_time()
                    elif get_current_time() > Parameter.period2_start_lighting and get_current_time() < Parameter.period2_stop_lighting:
                        if Outdoor.radiation < Parameter.radiation2_to_open_lighting:
                            Control.set_lighting_1("on")
                            open_time2 = get_time()

            elif Control.get_lighting_1() == "on" and Control.get_lighting_2() == "off":
                t1 = int(get_time() - open_time)
                t2 = int(get_time() - open_time2)
                if t1 > 1750 and t1 < 1850:
                    Control.set_lighting_2("on")
                if t2 > 1750 and t2 < 1850:
                    Control.set_lighting_2("on")

            elif Control.get_lighting_1() == "on" and Control.get_lighting_2() == "on":
                if get_current_time() > Parameter.period1_start_lighting and get_current_time() < Parameter.period1_stop_lighting:
                    if Outdoor.radiation > Parameter.radiation1_to_open_lighting:
                        Control.set_lighting_1("off")
                        stop_time = get_time()
                elif get_current_time() > Parameter.period2_start_lighting and get_current_time() < Parameter.period2_stop_lighting:
                    if Outdoor.radiation > Parameter.radiation2_to_open_lighting:
                        Control.set_lighting_1("off")
                        stop_time2 = get_time()
                else:
                    Control.set_lighting_1("off")
                    stop_time3 = get_time()

            elif Control.get_lighting_1() == "off" and Control.get_lighting_2() == "on":
                t3 = get_time() - stop_time3
                t4 = get_time() - stop_time2
                t5 = get_time() - stop_time
                if t3 > 1750 and t3 < 1850:
                    Control.set_lighting_2("off")
                if t4 > 1750 and t4 < 1850:
                    Control.set_lighting_2("off")
                if t5 > 1750 and t5 < 1850:
                    Control.set_lighting_2("off")


i = Indoor()
o = Outdoor()
c = Control()
gh = Ghauto()
p = Parameter()
gh.heating(i, p, c)
print c.get_heating()