'''

@author: Zxh
'''
from parameter import Parameter
import json

p = Parameter()


def get_json_value(obj, Parameter):
    keys = obj.keys()
    for key in keys:
        value = obj.get(key)
        setattr(Parameter, "_Parameter__" + key, value)
        print key, getattr(Parameter, "_Parameter__" + key)
    return Parameter

# data=p.build_to_json()
# print data
data = '''{       "update_time":"",
           "plant_parameter_setting":{
                                "time1":"1", 
                                "temperature1":"2",
                                "time2":"3",
                                "temperature2":"4",
                                "time3":"",
                                "temperature3":"5",
                                "time4":"",
                                "temperature4":"6"
                                      },
           "co2_parameter_setting":{
                                "co2_upper_limit":"2",
                                "co2_lower_limit":"9"
                                    },
           "cooling_fans":{
                          "cooling_start_temperature":"3",
                          "cooling_stop_temperature":"8"
                          },
           "roof_vent_parameter_setting":{
                                "expect_humidity":"",  
                                "humidity_influence_range_of_air_temperature":"4", 
                                "low_humidity_influence_on_air_temperature":"7",
                                "high_humidity_influence_on_air_temperature":"",
                                "expect_light":"",
                                "light_influence_on_air_temperature_slope":"",
                                "high_light_influence_on_temperature":"",
                                "low_light_influence_on_temperature":"",
                                "frost_temperature":"",
                                "indoor_temperature_lower_limit":"",
                                "roof_vent_wind_speed_upper_limit":"",
                                "roof_vent_rain_upper_limit":""
                                          },
           "heating_parameter_setting":{
                                "heating_start_lowest_temperature":"5",
                                "heating_stop_highest_temperature":""
                                        },
           "thermal_screen_parameter_setting":{
                                        "month_to_open_thermal_screen":"6",
                                        "month_to_close_thermal_screen":"",
                                        "time_to_open_thermal_screen":"",
                                        "time_to_close_thermal_screen":""
                                               },
           "side_vent_parameter_setting":{
                                    "temperature_to_open_side":"7",
                                    "wait_time_to_open_side":"",
                                    "rain_upper_limit_to_close":""
                                          },
           "other_parameter_setting":{
                             "upper_limit_light_to_open_shade_screen_out" :"8" ,
                             "upper_limit_light_to_open_shade_screen_in" :"",
                             "soil_humidity_to_start_irrigation":"",
                             "soil_humidity_to_stop_irrigation":"",
                             "temperature_to_open_fogging":"",
                             "temperature_to_open_cooling_pad":""
                                      },
            "lighting_setting":{
                    "month_to_open_lighting":"9",
                    "month_to_close_lighting":"",
                    "period1_start_lighting":"",
                    "period1_stop_lighting":"",
                    "period2_start_lighting":"",
                    "period2_stop_lighting":"",
                    "radiation1_to_open_lighting":"",
                    "radiation2_to_open_lighting":""
                        },
             "time_that_full_open_to_full_close":{
                        "roof_vent_open_time":"10",
                        "side_vent_open_time":"",
                        "shade_screen_out_open_time":"",
                        "shade_screen_in_open_time":"",
                        "thermal_screen_open_time":""
                             }
           }    '''

# obj=json.loads(data)
# print obj['plant_parameter_setting']
# p=get_json_value(obj['plant_parameter_setting'], p)
p = p.handle_post_parameter(data)
# print obj['plant_parameter_setting']['time1']
print p.get_time_1()
print p.get_co_2_upper_limit()
print p.get_cooling_start_temperature()
print p.get_humidity_influence_range_of_air_temperature()
print p.get_heating_start_lowest_temperature()
print p.get_month_to_open_thermal_screen()
print p.get_temperature_to_open_side()
print p.get_upper_limit_light_to_open_shade_screen_out()
print p.get_month_to_open_lighting()
print p.get_roof_vent_open_time()


