'''

@author: Zxh
'''
from currenttime import get_current_hour, get_current_month, get_time, get_current_time

from relay_output import bi_state_relay_output, tri_state_relay_output
from time import sleep


def auto_run_main(Indoor, Outdoor, Control, Parameter):
    init_parameter()
    get_current_control_state(Control)
    co2_control(Indoor, Parameter)
    shade_screen_out_control(Outdoor, Parameter)
    cooling_pad_control(Indoor, Parameter)
    fogging_control(Indoor, Parameter)
    roof_vent_control(Outdoor, Parameter, Indoor)
    side_vent_control(Indoor, Parameter)
    thermal_screen_control(Outdoor, Parameter)
    heating_control(Indoor, Parameter)
    shade_screen_in_control(Outdoor, Parameter)
    lighting_control(Control, Outdoor, Parameter)


# indoor temperature humidity, light

def init_parameter():
    global now_time, temperature_set_temp0, temperature_set_temp1, temperature_set_temp2, side_wait_time, lighting_open_time, lighting_open_time2, lighting_stop_time, lighting_stop_time2, lighting_stop_time3
    global bad_weather
    now_time = get_current_time()
    temperature_set_temp0 = 0
    temperature_set_temp1 = 0
    temperature_set_temp2 = 0
    side_wait_time = 0.0

    lighting_open_time = "0"
    lighting_open_time2 = "0"
    lighting_stop_time = "0"
    lighting_stop_time2 = "0"
    lighting_stop_time3 = "0"

    bad_weather = "true"


def get_current_control_state(Control):
    global auto_roof_vent_south, auto_roof_vent_north, auto_side_vent, auto_shade_screen_out, auto_shade_screen_in, auto_thermal_screen, auto_cooling_pad, auto_fogging, auto_heating, auto_co2
    global auto_lighting_1, auto_lighting_2, auto_irrigation
    auto_cooling_pad = Control.get_cooling_pad()
    auto_roof_vent_south = Control.get_roof_vent_south()
    auto_roof_vent_north = Control.get_roof_vent_north()
    auto_side_vent = Control.get_side_vent()
    auto_shade_screen_out = Control.get_shade_screen_out()
    auto_shade_screen_in = Control.get_shade_screen_in()
    auto_thermal_screen = Control.get_thermal_screen()
    auto_cooling_pad = Control.get_cooling_pad()
    auto_fogging = Control.get_fogging()
    auto_heating = Control.get_heating()
    auto_co2 = Control.get_co2()


#     auto_lighting_1 = Control.get_lighting_1()
#     auto_lighting_2 = Control.get_lighting_2()
#     auto_irrigation = Control.get_irrigation()

def co2_control(Indoor, Parameter):
    global auto_co2
    if Indoor.get_co2() < Parameter.get_co_2_lower_limit():
        bi_state_relay_output("co2", "on")
        auto_co2 = "on"
    elif Indoor.get_co2() > Parameter.get_co_2_upper_limit():
        bi_state_relay_output("co2", "off")
        auto_co2 = "off"


def shade_screen_out_control(Outdoor, Parameter):
    global auto_shade_screen_out
    if bad_weather == "true":
        if auto_shade_screen_out == "on":
            tri_state_relay_output("shade_screen_out", "off")
            wait_and_stop("shade_screen_out", Parameter.get_shade_screen_out_time(), "all")
        auto_shade_screen_out = "off"
    #         self.control.set_shade_screen_out("off")
    elif Outdoor.get_radiation() > Parameter.get_upper_limit_light_to_open_shade_screen_out():
        if auto_shade_screen_out == "off":
            tri_state_relay_output("shade_screen_out", "on")
            wait_and_stop("shade_screen_out", Parameter.get_shade_screen_out_time(), "all")
        #         self.control.set_shade_screen_out("off")
        auto_shade_screen_out = "on"
    #         self.control.set_shade_screen_out("on")
    else:
        if auto_shade_screen_out == "on":
            tri_state_relay_output("shade_screen_out", "off")
            wait_and_stop("shade_screen_out", Parameter.get_shade_screen_out_time(), "all")
        auto_shade_screen_out = "off"


#         self.control.set_shade_screen_out("off")

def cooling_pad_control(Indoor, Parameter):
    global auto_cooling_pad
    if float(Indoor.get_temperature()) > float(Parameter.get_temperature_to_open_cooling_pad()) + 1:
        bi_state_relay_output("cooling_pad", "on")
        auto_cooling_pad = "on"
    #         self.control.set_cooling_pad("on")
    elif float(Indoor.get_temperature()) < float(Parameter.get_temperature_to_open_cooling_pad()) - 1:
        bi_state_relay_output("cooling_pad", "off")
        auto_cooling_pad = "off"


#         self.control.set_cooling_pad("off")

def fogging_control(Indoor, Parameter):
    if float(Indoor.get_temperature()) > float(Parameter.get_temperature_to_open_fogging()) + 1:
        bi_state_relay_output("fogging", "on")
        auto_fogging = "on"
    #         Control.set_fogging("on")
    # if Control.get_thermal_screen()=="on"
    #    Control.set_thermal_screen("off")
    elif float(Indoor.get_temperature()) < float(Parameter.get_temperature_to_open_fogging()) - 1:
        bi_state_relay_output("fogging", "off")
        auto_fogging = "off"


#             Control.set_fogging("off")

def roof_vent_control(Outdoor, Parameter, Indoor):
    global temperature_set_temp0, temperature_set_temp1, temperature_set_temp2, angle, auto_roof_vent_north, auto_roof_vent_south
    if bad_weather == "true":
        if auto_roof_vent_north == "on" and auto_roof_vent_south == "on":
            tri_state_relay_output("roof_vent_south", "off")
            tri_state_relay_output("roof_vent_north", "off")
            wait_and_stop("roof_vent_south", Parameter.get_roof_vent_open_time(), "all")
            wait_and_stop("roof_vent_north", Parameter.get_roof_vent_open_time(), "all")
        auto_roof_vent_north = "off"
        auto_roof_vent_south = "off"
    #         self.control.set_roof_vent_north("off")
    #         self.control.set_roof_vent_south("off")
    else:
        if now_time >= Parameter.get_time_1() and now_time < Parameter.get_time_2():
            temperature_set_temp0 = float(Parameter.get_temperature_1())
        elif now_time >= Parameter.get_time_2() and now_time < Parameter.get_time_3():
            temperature_set_temp0 = float(Parameter.get_temperature_2())
        elif now_time >= Parameter.get_time_3() and now_time < Parameter.get_time_4():
            temperature_set_temp0 = float(Parameter.get_temperature_3())
        else:
            temperature_set_temp0 = float(Parameter.get_temperature_4())

            #humidity influence on temperature
        if float(Parameter.get_humidity_influence_range_of_air_temperature()) == 0:
            print "humidity_influence_range_of_air_temperature can not be 0"
        elif float(Parameter.get_expect_humidity()) == 95:
            print "expect_humidity can not be 95%"
        else:
            if float(Outdoor.get_humidity()) <= (float(Parameter.get_expect_humidity()) - 5 - float(
                    Parameter.get_humidity_influence_range_of_air_temperature())):
                temperature_set_temp1 = temperature_set_temp0 + float(
                    Parameter.get_low_humidity_influence_on_air_temperature())
            elif float(Outdoor.get_humidity()) <= (float(Parameter.get_expect_humidity()) - 5):
                tmpt = (float(Parameter.get_expect_humidity()) - 5 - float(Outdoor.get_humidity())) * float(
                    Parameter.get_low_humidity_influence_on_air_temperature()) / float(
                    Parameter.get_humidity_influence_range_of_air_temperature())
                temperature_set_temp1 = temperature_set_temp0 + tmpt
            elif float(Outdoor.get_humidity()) >= (float(Parameter.get_expect_humidity()) + 5):
                tmpt = (float(Outdoor.get_humidity()) - float(Parameter.get_expect_humidity()) - 5) * float(
                    Parameter.get_high_humidity_influence_on_air_temperature()) / (
                       100 - 5 - float(Parameter.get_expect_humidity()))
                temperature_set_temp1 = temperature_set_temp0 + tmpt
            else:
                temperature_set_temp1 = temperature_set_temp0

        #light influence on temperature
        if Outdoor.get_radiation() < Parameter.get_expect_light():
            temperature_set_temp2 = temperature_set_temp1
        else:
            temperature_set_temp2 = temperature_set_temp1 - float(
                Parameter.get_light_influence_on_air_temperature_slope()) * (float(Outdoor.get_radiation()) - float(
                Parameter.get_expect_light()))
        if temperature_set_temp2 > (temperature_set_temp1 + float(Parameter.get_low_light_influence_on_temperature())):
            temperature_set_temp2 = temperature_set_temp1 + float(Parameter.get_low_light_influence_on_temperature())
        elif temperature_set_temp2 < (
            temperature_set_temp1 - float(Parameter.get_high_light_influence_on_temperature())):
            temperature_set_temp2 = temperature_set_temp1 - float(Parameter.get_high_light_influence_on_temperature())
        else:
            if temperature_set_temp2 == 0:
                temperature_set_temp2 = 0

        if Outdoor.get_temperature() <= Parameter.get_frost_temperature():
            if auto_roof_vent_north == "on" and auto_roof_vent_south == "on":
                tri_state_relay_output("roof_vent_south", "off")
                tri_state_relay_output("roof_vent_north", "off")
                wait_and_stop("roof_vent_south", Parameter.get_roof_vent_open_time(), "all")
                wait_and_stop("roof_vent_north", Parameter.get_roof_vent_open_time(), "all")
            auto_roof_vent_north = "off"
            auto_roof_vent_south = "off"
        #             Control.set_roof_vent_north("off")
        #             Control.set_roof_vent_south("off")
        elif Outdoor.get_temperature() <= Parameter.get_indoor_temperature_lower_limit():
            #small angle
            if auto_roof_vent_north == "off" and auto_roof_vent_south == "off":
                tri_state_relay_output("roof_vent_south", "on")
                tri_state_relay_output("roof_vent_north", "on")
                wait_and_stop("roof_vent_south", Parameter.get_roof_vent_open_time(), "small")
                wait_and_stop("roof_vent_north", Parameter.get_roof_vent_open_time(), "small")
            auto_roof_vent_north = "on"
            auto_roof_vent_south = "on"
            angle = "small"
        #             Control.set_roof_vent_north("on")
        #             Control.set_roof_vent_south("on")
        elif Outdoor.get_temperature() <= temperature_set_temp2:
            #open all
            if auto_roof_vent_north == "off" and auto_roof_vent_south == "off":
                tri_state_relay_output("roof_vent_south", "on")
                tri_state_relay_output("roof_vent_north", "on")
                wait_and_stop("roof_vent_south", Parameter.get_roof_vent_open_time(), "half")
                wait_and_stop("roof_vent_north", Parameter.get_roof_vent_open_time(), "half")
            auto_roof_vent_north = "on"
            auto_roof_vent_south = "on"
            angle = "half"
        #             Control.set_roof_vent_north("on")
        #             Control.set_roof_vent_south("on")
        else:
            #  
            if auto_roof_vent_north == "off" and auto_roof_vent_south == "off":
                tri_state_relay_output("roof_vent_south", "on")
                tri_state_relay_output("roof_vent_north", "on")
                wait_and_stop("roof_vent_south", Parameter.get_roof_vent_open_time(), "all")
                wait_and_stop("roof_vent_north", Parameter.get_roof_vent_open_time(), "all")
            auto_roof_vent_north = "on"
            auto_roof_vent_south = "on"
            angle = "all"


#             Control.set_roof_vent_north("on")
#             Control.set_roof_vent_south("on")

def get_side_wait_time(Indoor, Parameter):
    if Indoor.get_temperature() > (temperature_set_temp2 + Parameter.get_temperature_to_open_side()):
        if side_wait_time < Parameter.get_wait_time_to_open_side():
            side_wait_time += 1


def side_vent_control(Indoor, Parameter):
    global auto_side_vent, side_wait_time
    if bad_weather == "true":
        if auto_side_vent == "on":
            tri_state_relay_output("side_vent", "off")
            wait_and_stop("side_vent", Parameter.get_side_vent_time(), "all")
        auto_side_vent = "off"
    #         control.set_side_vent("off")
    elif auto_cooling_pad == "on":
        if auto_side_vent == "off":
            tri_state_relay_output("side_vent", "on")
            wait_and_stop("side_vent", Parameter.get_side_vent_time(), "all")
        auto_side_vent = "on"
    #         control.set_side_vent("on")
    elif auto_roof_vent_north == "on" and auto_roof_vent_south == "on":
        if side_wait_time < int(Parameter.get_wait_time_to_open_side()):
            #             control.set_side_vent("off")
            if auto_side_vent == "on":
                tri_state_relay_output("side_vent", "off")
                wait_and_stop("side_vent", Parameter.get_side_vent_time(), "all")
            auto_side_vent = "off"
        elif side_wait_time > float(Parameter.get_wait_time_to_open_side()) and side_wait_time < 2 * float(
                Parameter.get_wait_time_to_open_side()):
            #half open
            if auto_side_vent == "off":
                tri_state_relay_output("side_vent", "on")
                wait_and_stop("side_vent", Parameter.get_side_vent_time(), "half")
            auto_side_vent = "on"
        #             control.set_side_vent("on")
        elif side_wait_time > 2 * float(Parameter.get_wait_time_to_open_side()):
            #open
            if auto_side_vent == "off":
                tri_state_relay_output("side_vent", "on")
                wait_and_stop("side_vent", Parameter.get_side_vent_time(), "all")
            auto_side_vent = "on"
        #             control.set_side_vent("on")
        elif Indoor.get_temperature() < (temperature_set_temp2 + float(Parameter.get_temperature_to_open_side())):
            if auto_side_vent == "on":
                tri_state_relay_output("side_vent", "off")
                wait_and_stop("side_vent", Parameter.get_side_vent_time(), "all")
            auto_side_vent = "off"
            side_wait_time = 0


#         control.set_side_vent("off")

def thermal_screen_control(Outdoor, Parameter):
    global auto_thermal_screen
    if bad_weather == "true":
        if auto_thermal_screen == "on":
            tri_state_relay_output("thermal_screen", "off")
            wait_and_stop("side_vent", Parameter.get_thermal_screen_open_time(), "all")
        auto_thermal_screen = "off"
    #         control.set_thermal_screen("off")
    elif auto_fogging == "on":
        if auto_thermal_screen == "on":
            tri_state_relay_output("thermal_screen", "off")
            wait_and_stop("side_vent", Parameter.get_thermal_screen_open_time(), "all")
        auto_thermal_screen = "off"
    #         control.set_thermal_screen("off")
    else:
        current_hour = get_current_hour()
        current_month = get_current_month()
        if current_month > Parameter.get_month_to_open_thermal_screen() and current_month < Parameter.get_month_to_close_thermal_screen():
            if current_hour > Parameter.get_time_to_open_thermal_screen() and current_hour < Parameter.get_time_to_close_thermal_screen():
                if auto_thermal_screen == "off":
                    tri_state_relay_output("thermal_screen", "on")
                    wait_and_stop("side_vent", Parameter.get_thermal_screen_open_time(), "all")
                auto_thermal_screen = "on"
            #                 control.set_thermal_screen("off")    #open
        else:
            if auto_thermal_screen == "on":
                tri_state_relay_output("thermal_screen", "off")
                wait_and_stop("side_vent", Parameter.get_thermal_screen_open_time(), "all")
            auto_thermal_screen = "off"
            #             control.set_thermal_screen("on")


def heating_control(Indoor, Parameter):  #ok
    if Indoor.get_temperature() < Parameter.get_heating_start_lowest_temperature():
        bi_state_relay_output("heating", "on")
    #         self.control.set_heating("on")
    elif Indoor.get_temperature() > Parameter.get_heating_stop_highest_temperature():
        bi_state_relay_output("heating", "on")


#         self.control.set_heating("off")

def shade_screen_in_control(Outdoor, Parameter):
    global auto_shade_screen_in
    if auto_thermal_screen == "on":
        if auto_shade_screen_in == "off":
            tri_state_relay_output("shade_screen_in", "on")
            wait_and_stop("shade_screen_in", Parameter.get_shade_screen_in_time(), "all")
        auto_shade_screen_in = "on"
    #         self.control.set_shade_screen_in("on")
    elif Outdoor.get_radiation() > Parameter.get_upper_limit_light_to_open_shade_screen_in():
        #         self.control.set_shade_screen_in("off")
        if auto_shade_screen_in == "on":
            tri_state_relay_output("shade_screen_in", "off")
            wait_and_stop("shade_screen_in", Parameter.get_shade_screen_in_time(), "all")
        auto_shade_screen_in = "off"
    else:
        if auto_shade_screen_in == "off":
            tri_state_relay_output("shade_screen_in", "on")
            wait_and_stop("shade_screen_in", Parameter.get_shade_screen_in_time(), "all")
        auto_shade_screen_in = "on"


#         self.control.set_shade_screen_in("on")

def lighting_control(Control, Outdoor, Parameter):
    global lighting_stop_time, lighting_stop_time2, lighting_stop_time3
    auto_lighting_1 = Control.get_lighting_1()
    auto_lighting_2 = Control.get_lighting_2()
    if auto_lighting_1 == "off" and auto_lighting_2 == "off":
        if get_current_month() > Parameter.get_month_to_open_lighting() and get_current_month() < Parameter.get_month_to_close_lighting():
            if get_current_time() > Parameter.get_period_1_start_lighting() and get_current_time() < Parameter.get_period_1_stop_lighting():
                if Outdoor.get_radiation() < Parameter.get_radiation_1_to_open_lighting():
                    #                         Control.set_lighting_1("on")
                    bi_state_relay_output("lighting_1", "on")
                    auto_lighting_1 = "on"
                    lighting_open_time = get_time()
            elif get_current_time() > Parameter.get_period_2_start_lighting() and get_current_time() < Parameter.get_period_2_stop_lighting():
                if Outdoor.get_radiation() < Parameter.get_radiation_2_to_open_lighting():
                    #                         Control.set_lighting_1("on")
                    bi_state_relay_output("lighting_2", "on")
                    auto_lighting_2 = "on"
                    lighting_open_time2 = get_time()

    elif auto_lighting_1 == "on" and auto_lighting_2 == "off":
        t1 = int(get_time() - lighting_open_time)
        t2 = int(get_time() - lighting_open_time2)
        if t1 > 1750 and t1 < 1850:
            bi_state_relay_output("ligting_2", "on")
            auto_lighting_2 = "on"
        #                 Control.set_lighting_2("on")
        if t2 > 1750 and t2 < 1850:
            #                 Control.set_lighting_2("on")
            bi_state_relay_output("ligting_2", "on")
            auto_lighting_2 = "on"
    elif auto_lighting_1 == "on" and auto_lighting_2 == "on":
        if get_current_time() > Parameter.get_period_1_start_lighting() and get_current_time() < Parameter.get_period_1_stop_lighting():
            if Outdoor.get_radiation() > Parameter.get_radiation_1_to_open_lighting():
                #                     Control.set_lighting_1("off")
                bi_state_relay_output("ligting_1", "off")
                auto_lighting_1 = "off"
                lighting_stop_time = get_time()
        elif get_current_time() > Parameter.get_period_2_start_lighting() and get_current_time() < Parameter.get_period_2_stop_lighting():
            if Outdoor.get_radiation() > Parameter.get_radiation_2_to_open_lighting():
                #                     Control.set_lighting_1("off")
                bi_state_relay_output("ligting_1", "off")
                auto_lighting_1 = "off"
                lighting_stop_time2 = get_time()
        else:
            #                 Control.set_lighting_1("off")
            bi_state_relay_output("ligting_1", "off")
            auto_lighting_1 = "off"
            lighting_stop_time3 = get_time()

    elif auto_lighting_1 == "off" and auto_lighting_2 == "on":
        t3 = get_time() - lighting_stop_time3
        t4 = get_time() - lighting_stop_time2
        t5 = get_time() - lighting_stop_time
        if t3 > 1750 and t3 < 1850:
            bi_state_relay_output("ligting_2", "off")
        #                 Control.set_lighting_2("off")
        if t4 > 1750 and t4 < 1850:
            bi_state_relay_output("ligting_2", "off")
        #                 Control.set_lighting_2("off")
        if t5 > 1750 and t5 < 1850:
            bi_state_relay_output("ligting_2", "off")
        #                 Control.set_lighting_2("off")
    else:
        bi_state_relay_output("ligting_2", "off")
        bi_state_relay_output("ligting_1", "off")


def wait_and_stop(key, time, open_all):
    time = int(time)
    if open_all == "all":
        sleep(time)
    elif open_all == "half":
        sleep(time / 2)
    elif open_all == "small":
        sleep(time / 4)
    else:
        sleep(2)
    tri_state_relay_output(key, "stop")
