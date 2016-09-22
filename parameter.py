'''

@author: Zxh
'''
from currenttime import get_current_time
import json


class Parameter(object):
    plant_parameter = (
        'time1', 'time2', 'time3', 'time4', 'temperature1', 'temperature2', 'temperature3', 'temperature4')
    co2_parameter = ('co2_upper_limit', 'co2_lower_limit')
    cool_fans_parameter = ('cooling_start_temperature', 'cooling_stop_temperature')
    roof_vent_parameter = (
        'expect_humidity', 'humidity_influence_range_of_air_temperature', 'low_humidity_influence_on_air_temperature',
        'high_humidity_influence_on_air_temperature', 'expect_light',
        'light_influence_on_air_temperature_slope', 'high_light_influence_on_temperature',
        'low_light_influence_on_temperature', 'frost_temperature', 'indoor_temperature_lower_limit',
        'roof_vent_wind_speed_upper_limit', 'roof_vent_rain_upper_limit')
    heating_parameter = ('heating_start_lowest_temperature', 'heating_stop_highest_temperature')
    thermal_screen_parameter = (
        'month_to_open_thermal_screen', 'month_to_close_thermal_screen', 'time_to_open_thermal_screen',
        'time_to_close_thermal_screen')
    side_vent_parameter = ('temperature_to_open_side', 'wait_time_to_open_side', 'rain_upper_limit_to_close')
    other_parameter = ('upper_limit_light_to_open_out_shade_screen', 'upper_limit_light_to_open_in_shade_screen',
                       'soil_humidity_to_start_irrigation', 'soil_humidity_to_stop_irrigation',
                       'temperature_to_open_fogging'
                       'temperature_to_open_cooling_pad')
    lighting_parameter = (
        'month_to_open_lighting', 'month_to_close_lighting', 'period1_start_lighting', 'period1_stop_lighting',
        'period2_start_lighting', 'period2_stop_lighting', 'radiation1_to_open_lighting', 'radiation2_to_open_lighting')
    time_that_full_open_to_full_close_parameter = (
        'roof_vent_open_time', 'side_vent_open_time', 'shade_screen_out_open_time', 'shade_screen_in_open_time',
        'thermal_screen_open_time')

    def __init__(self):
        self.update_time = ""
        self.__time1 = ""
        self.__temperature1 = ""
        self.__time2 = ""
        self.__temperature2 = ""
        self.__time3 = ""
        self.__temperature3 = ""
        self.__time4 = ""
        self.__temperature4 = ""

        self.__co2_upper_limit = ""
        self.__co2_lower_limit = ""

        self.__cooling_start_temperature = ""
        self.__cooling_stop_temperature = ""

        self.__expect_humidity = ""
        self.__humidity_influence_range_of_air_temperature = ""
        self.__low_humidity_influence_on_air_temperature = ""
        self.__high_humidity_influence_on_air_temperature = ""
        self.__expect_light = ""
        self.__light_influence_on_air_temperature_slope = ""
        self.__high_light_influence_on_temperature = ""
        self.__low_light_influence_on_temperature = ""
        self.__frost_temperature = ""
        self.__indoor_temperature_lower_limit = ""
        self.__roof_vent_wind_speed_upper_limit = ""
        self.__roof_vent_rain_upper_limit = ""

        self.__heating_start_lowest_temperature = ""
        self.__heating_stop_highest_temperature = ""

        self.__month_to_open_thermal_screen = ""
        self.__month_to_close_thermal_screen = ""
        self.__time_to_open_thermal_screen = ""
        self.__time_to_close_thermal_screen = ""

        self.__temperature_to_open_side = ""
        self.__wait_time_to_open_side = ""
        self.__rain_upper_limit_to_close = ""

        self.__upper_limit_light_to_open_out_shade_screen = ""
        self.__upper_limit_light_to_open_in_shade_screen = ""
        self.__soil_humidity_to_start_irrigation = ""
        self.__soil_humidity_to_stop_irrigation = ""
        self.__temperature_to_open_fogging = ""
        self.__temperature_to_open_cooling_pad = ""

        self.__month_to_open_lighting = ""
        self.__month_to_close_lighting = ""
        self.__period1_start_lighting = ""
        self.__period1_stop_lighting = ""
        self.__period2_start_lighting = ""
        self.__period2_stop_lighting = ""
        self.__radiation1_to_open_lighting = ""
        self.__radiation2_to_open_lighting = ""

        self.__roof_vent_open_time = ""
        self.__side_vent_open_time = ""
        self.__shade_screen_out_open_time = ""
        self.__shade_screen_in_open_time = ""
        self.__thermal_screen_open_time = ""

    def get_time_1(self):
        return self.__time1

    def get_temperature_1(self):
        return self.__temperature1

    def get_time_2(self):
        return self.__time2

    def get_temperature_2(self):
        return self.__temperature2

    def get_time_3(self):
        return self.__time3

    def get_temperature_3(self):
        return self.__temperature3

    def get_time_4(self):
        return self.__time4

    def get_temperature_4(self):
        return self.__temperature4

    def get_co_2_upper_limit(self):
        return self.__co2_upper_limit

    def get_co_2_lower_limit(self):
        return self.__co2_lower_limit

    def get_cooling_start_temperature(self):
        return self.__cooling_start_temperature

    def get_cooling_stop_temperature(self):
        return self.__cooling_stop_temperature

    def get_expect_humidity(self):
        return self.__expect_humidity

    def get_humidity_influence_range_of_air_temperature(self):
        return self.__humidity_influence_range_of_air_temperature

    def get_low_humidity_influence_on_air_temperature(self):
        return self.__low_humidity_influence_on_air_temperature

    def get_high_humidity_influence_on_air_temperature(self):
        return self.__high_humidity_influence_on_air_temperature

    def get_expect_light(self):
        return self.__expect_light

    def get_light_influence_on_air_temperature_slope(self):
        return self.__light_influence_on_air_temperature_slope

    def get_high_light_influence_on_temperature(self):
        return self.__high_light_influence_on_temperature

    def get_low_light_influence_on_temperature(self):
        return self.__low_light_influence_on_temperature

    def get_frost_temperature(self):
        return self.__frost_temperature

    def get_indoor_temperature_lower_limit(self):
        return self.__indoor_temperature_lower_limit

    def get_roof_vent_wind_speed_upper_limit(self):
        return self.__roof_vent_wind_speed_upper_limit

    def get_roof_vent_rain_upper_limit(self):
        return self.__roof_vent_rain_upper_limit

    def get_heating_start_lowest_temperature(self):
        return self.__heating_start_lowest_temperature

    def get_heating_stop_highest_temperature(self):
        return self.__heating_stop_highest_temperature

    def get_month_to_open_thermal_screen(self):
        return self.__month_to_open_thermal_screen

    def get_month_to_close_thermal_screen(self):
        return self.__month_to_close_thermal_screen

    def get_time_to_open_thermal_screen(self):
        return self.__time_to_open_thermal_screen

    def get_time_to_close_thermal_screen(self):
        return self.__time_to_close_thermal_screen

    def get_temperature_to_open_side(self):
        return self.__temperature_to_open_side

    def get_wait_time_to_open_side(self):
        return self.__wait_time_to_open_side

    def get_rain_upper_limit_to_close(self):
        return self.__rain_upper_limit_to_close

    def get_upper_limit_light_to_open_out_shade_screen(self):
        return self.__upper_limit_light_to_open_out_shade_screen

    def get_upper_limit_light_to_open_in_shade_screen(self):
        return self.__upper_limit_light_to_open_in_shade_screen

    def get_soil_humidity_to_start_irrigation(self):
        return self.__soil_humidity_to_start_irrigation

    def get_soil_humidity_to_stop_irrigation(self):
        return self.__soil_humidity_to_stop_irrigation

    def get_temperature_to_open_fogging(self):
        return self.__temperature_to_open_fogging

    def get_temperature_to_open_cooling_pad(self):
        return self.__temperature_to_open_cooling_pad

    def get_month_to_open_lighting(self):
        return self.__month_to_open_lighting

    def get_month_to_close_lighting(self):
        return self.__month_to_close_lighting

    def get_period_1_start_lighting(self):
        return self.__period1_start_lighting

    def get_period_1_stop_lighting(self):
        return self.__period1_stop_lighting

    def get_period_2_start_lighting(self):
        return self.__period2_start_lighting

    def get_period_2_stop_lighting(self):
        return self.__period2_stop_lighting

    def get_radiation_1_to_open_lighting(self):
        return self.__radiation1_to_open_lighting

    def get_radiation_2_to_open_lighting(self):
        return self.__radiation2_to_open_lighting

    def get_roof_vent_open_time(self):
        return self.__roof_vent_open_time

    def get_side_vent_open_time(self):
        return self.__side_vent_open_time

    def get_shade_screen_out_open_time(self):
        return self.__shade_screen_out_open_time

    def get_shade_screen_in_open_time(self):
        return self.__shade_screen_in_open_time

    def get_thermal_screen_open_time(self):
        return self.__thermal_screen_open_time

    def set_time_1(self, value):
        self.__time1 = value

    def set_temperature_1(self, value):
        self.__temperature1 = value

    def set_time_2(self, value):
        self.__time2 = value

    def set_temperature_2(self, value):
        self.__temperature2 = value

    def set_time_3(self, value):
        self.__time3 = value

    def set_temperature_3(self, value):
        self.__temperature3 = value

    def set_time_4(self, value):
        self.__time4 = value

    def set_temperature_4(self, value):
        self.__temperature4 = value

    def set_co_2_upper_limit(self, value):
        self.__co2_upper_limit = value

    def set_co_2_lower_limit(self, value):
        self.__co2_lower_limit = value

    def set_cooling_start_temperature(self, value):
        self.__cooling_start_temperature = value

    def set_cooling_stop_temperature(self, value):
        self.__cooling_stop_temperature = value

    def set_expect_humidity(self, value):
        self.__expect_humidity = value

    def set_humidity_influence_range_of_air_temperature(self, value):
        self.__humidity_influence_range_of_air_temperature = value

    def set_low_humidity_influence_on_air_temperature(self, value):
        self.__low_humidity_influence_on_air_temperature = value

    def set_high_humidity_influence_on_air_temperature(self, value):
        self.__high_humidity_influence_on_air_temperature = value

    def set_expect_light(self, value):
        self.__expect_light = value

    def set_light_influence_on_air_temperature_slope(self, value):
        self.__light_influence_on_air_temperature_slope = value

    def set_high_light_influence_on_temperature(self, value):
        self.__high_light_influence_on_temperature = value

    def set_low_light_influence_on_temperature(self, value):
        self.__low_light_influence_on_temperature = value

    def set_frost_temperature(self, value):
        self.__frost_temperature = value

    def set_indoor_temperature_lower_limit(self, value):
        self.__indoor_temperature_lower_limit = value

    def set_roof_vent_wind_speed_upper_limit(self, value):
        self.__roof_vent_wind_speed_upper_limit = value

    def set_roof_vent_rain_upper_limit(self, value):
        self.__roof_vent_rain_upper_limit = value

    def set_heating_start_lowest_temperature(self, value):
        self.__heating_start_lowest_temperature = value

    def set_heating_stop_highest_temperature(self, value):
        self.__heating_stop_highest_temperature = value

    def set_month_to_open_thermal_screen(self, value):
        self.__month_to_open_thermal_screen = value

    def set_month_to_close_thermal_screen(self, value):
        self.__month_to_close_thermal_screen = value

    def set_time_to_open_thermal_screen(self, value):
        self.__time_to_open_thermal_screen = value

    def set_time_to_close_thermal_screen(self, value):
        self.__time_to_close_thermal_screen = value

    def set_temperature_to_open_side(self, value):
        self.__temperature_to_open_side = value

    def set_wait_time_to_open_side(self, value):
        self.__wait_time_to_open_side = value

    def set_rain_upper_limit_to_close(self, value):
        self.__rain_upper_limit_to_close = value

    def set_upper_limit_light_to_open_out_shade_screen(self, value):
        self.__upper_limit_light_to_open_out_shade_screen = value

    def set_upper_limit_light_to_open_in_shade_screen(self, value):
        self.__upper_limit_light_to_open_in_shade_screen = value

    def set_soil_humidity_to_start_irrigation(self, value):
        self.__soil_humidity_to_start_irrigation = value

    def set_soil_humidity_to_stop_irrigation(self, value):
        self.__soil_humidity_to_stop_irrigation = value

    def set_temperature_to_open_fogging(self, value):
        self.__temperature_to_open_fogging = value

    def set_temperature_to_open_cooling_pad(self, value):
        self.__temperature_to_open_cooling_pad = value

    def set_month_to_open_lighting(self, value):
        self.__month_to_open_lighting = value

    def set_month_to_close_lighting(self, value):
        self.__month_to_close_lighting = value

    def set_period_1_start_lighting(self, value):
        self.__period1_start_lighting = value

    def set_period_1_stop_lighting(self, value):
        self.__period1_stop_lighting = value

    def set_period_2_start_lighting(self, value):
        self.__period2_start_lighting = value

    def set_period_2_stop_lighting(self, value):
        self.__period2_stop_lighting = value

    def set_radiation_1_to_open_lighting(self, value):
        self.__radiation1_to_open_lighting = value

    def set_radiation_2_to_open_lighting(self, value):
        self.__radiation2_to_open_lighting = value

    def set_roof_vent_open_time(self, value):
        self.__roof_vent_open_time = value

    def set_side_vent_open_time(self, value):
        self.__side_vent_open_time = value

    def set_shade_screen_out_open_time(self, value):
        self.__shade_screen_out_open_time = value

    def set_shade_screen_in_open_time(self, value):
        self.__shade_screen_in_open_time = value

    def set_thermal_screen_open_time(self, value):
        self.__thermal_screen_open_time = value

    def handle_post_parameter(self, data):
        data = json.loads(data)
        self.update_time = data['update_time']
        co2_parameter_setting = data['co2_parameter_setting']
        plant_parameter_setting = data['plant_parameter_setting']
        cooling_fans = data['cooling_fans']
        roof_vent_parameter_setting = data['roof_vent_parameter_setting']
        heating_parameter_setting = data['heating_parameter_setting']
        thermal_screen_parameter_setting = data['thermal_screen_parameter_setting']
        side_vent_parameter_setting = data['side_vent_parameter_setting']
        other_parameter_setting = data['other_parameter_setting']
        lighting_setting = data['lighting_setting']
        time_that_full_open_to_full_close = data['time_that_full_open_to_full_close']

        self.get_json_value(plant_parameter_setting)
        self.get_json_value(co2_parameter_setting)
        self.get_json_value(cooling_fans)
        self.get_json_value(roof_vent_parameter_setting)
        self.get_json_value(heating_parameter_setting)
        self.get_json_value(thermal_screen_parameter_setting)
        self.get_json_value(side_vent_parameter_setting)
        self.get_json_value(other_parameter_setting)
        self.get_json_value(lighting_setting)
        self.get_json_value(time_that_full_open_to_full_close)

    # return self

    def build_to_json(self):
        return '''{       "update_time":"%s",
           "plant_parameter_setting":{
                                "time1":"%s", 
                                "temperature1":"%s",
                                "time2":"%s",
                                "temperature2":"%s",
                                "time3":"%s",
                                "temperature3":"%s",
                                "time4":"%s",
                                "temperature4":"%s"
                                      },
           "co2_parameter_setting":{
                                "co2_upper_limit":"%s",
                                "co2_lower_limit":"%s"
                                    },
           "cooling_fans":{
                          "cooling_start_temperature":"%s",
                          "cooling_stop_temperature":"%s"
                          },
           "roof_vent_parameter_setting":{
                                "expect_humidity":"%s",  
                                "humidity_influence_range_of_air_temperature":"%s", 
                                "low_humidity_influence_on_air_temperature":"%s",
                                "high_humidity_influence_on_air_temperature":"%s",
                                "expect_light":"%s",
                                "light_influence_on_air_temperature_slope":"%s",
                                "high_light_influence_on_temperature":"%s",
                                "low_light_influence_on_temperature":"%s",
                                "frost_temperature":"%s",
                                "indoor_temperature_lower_limit":"%s",
                                "roof_vent_wind_speed_upper_limit":"%s",
                                "roof_vent_rain_upper_limit":"%s"
                                          },
           "heating_parameter_setting":{
                                "heating_start_lowest_temperature":"%s",
                                "heating_stop_highest_temperature":"%s"
                                        },
           "thermal_screen_parameter_setting":{
                                        "month_to_open_thermal_screen":"%s",
                                        "month_to_close_thermal_screen":"%s",
                                        "time_to_open_thermal_screen":"%s",
                                        "time_to_close_thermal_screen":"%s"
                                               },
           "side_vent_parameter_setting":{
                                    "temperature_to_open_side":"%s",
                                    "wait_time_to_open_side":"%s",
                                    "rain_upper_limit_to_close":"%s"
                                          },
           "other_parameter_setting":{
                             "upper_limit_light_to_open_out_shade_screen" :"%s" ,
                             "upper_limit_light_to_open_in_shade_screen" :"%s",
                             "soil_humidity_to_start_irrigation":"%s",
                             "soil_humidity_to_stop_irrigation":"%s",
                             "temperature_to_open_fogging":"%s",
                             "temperature_to_open_cooling_pad":"%s"
                                      },
            "lighting_setting":{
                    "month_to_open_lighting":"%s",
                    "month_to_close_lighting":"%s",
                    "period1_start_lighting":"%s",
                    "period1_stop_lighting":"%s",
                    "period2_start_lighting":"%s",
                    "period2_stop_lighting":"%s",
                    "radiation1_to_open_lighting":"%s",
                    "radiation2_to_open_lighting":"%s"
                        },
             "time_that_full_open_to_full_close":{
                        "roof_vent_open_time":"%s",
                        "side_vent_open_time":"%s",
                        "shade_screen_out_open_time":"%s",
                        "shade_screen_in_open_time":"%s",
                        "thermal_screen_open_time":"%s"
                             }
           }                 
           ''' \
               % (get_current_time(),
                  self.get_time_1(),
                  self.get_temperature_1(),
                  self.get_time_2(),
                  self.get_temperature_2(),
                  self.get_time_3(),
                  self.get_temperature_3(),
                  self.get_time_4(),
                  self.get_temperature_4(),

                  self.get_co_2_upper_limit(),
                  self.get_co_2_lower_limit(),

                  self.get_cooling_start_temperature(),
                  self.get_cooling_stop_temperature(),

                  self.get_expect_humidity(),
                  self.get_humidity_influence_range_of_air_temperature(),
                  self.get_low_humidity_influence_on_air_temperature(),
                  self.get_high_humidity_influence_on_air_temperature(),
                  self.get_expect_light(),
                  self.get_light_influence_on_air_temperature_slope(),
                  self.get_high_light_influence_on_temperature(),
                  self.get_low_light_influence_on_temperature(),
                  self.get_frost_temperature(),
                  self.get_indoor_temperature_lower_limit(),
                  self.get_roof_vent_wind_speed_upper_limit(),
                  self.get_roof_vent_rain_upper_limit(),

                  self.get_heating_start_lowest_temperature(),
                  self.get_heating_stop_highest_temperature(),

                  self.get_month_to_open_thermal_screen(),
                  self.get_month_to_close_thermal_screen(),
                  self.get_time_to_open_thermal_screen(),
                  self.get_time_to_close_thermal_screen(),

                  self.get_temperature_to_open_side(),
                  self.get_wait_time_to_open_side(),
                  self.get_rain_upper_limit_to_close(),

                  self.get_upper_limit_light_to_open_out_shade_screen(),
                  self.get_upper_limit_light_to_open_in_shade_screen(),
                  self.get_soil_humidity_to_start_irrigation(),
                  self.get_soil_humidity_to_stop_irrigation(),
                  self.get_temperature_to_open_fogging(),
                  self.get_temperature_to_open_cooling_pad(),

                  self.get_month_to_open_lighting(),
                  self.get_month_to_close_lighting(),
                  self.get_period_1_start_lighting(),
                  self.get_period_1_stop_lighting(),
                  self.get_period_2_start_lighting(),
                  self.get_period_2_stop_lighting(),
                  self.get_radiation_1_to_open_lighting(),
                  self.get_radiation_2_to_open_lighting(),

                  self.get_roof_vent_open_time(),
                  self.get_side_vent_open_time(),
                  self.get_shade_screen_out_open_time(),
                  self.get_shade_screen_in_open_time(),
                  self.get_thermal_screen_open_time()
        )

    def get_json_value(self, obj):
        keys = obj.keys()
        for key in keys:
            value = obj.get(key)
            setattr(self, "_Parameter__" + key, value)
            #             print key,getattr(self,"_Parameter__"+key)
            #         return self

# test
# if __name__=='__main__':
# print Parameter().get_co2_lower_limit()
#     test=Parameter()
#     d="d"
#     test.set__side_vent_open_time(d)
#     print test.get_co_2_lower_limit()
#     print test.build_to_json()
