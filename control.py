import json
from currenttime import get_current_time
from CONTROL_CONSTANT import CONTROL_CONSTANT

class Control(object):
    '''the object of tri-state actuators and bi-state'''

    CONSTANT = CONTROL_CONSTANT()
    def __init__(self):
        self.__update_time = "2016/07/27 22:08:00"
        self.__roof_vent_south = 'on'
        self.__roof_vent_north = 'on'
        self.__side_vent = 'on'
        self.__shade_screen_north = 'on'
        self.__shade_screen_south = 'on'
        self.__thermal_screen = 'on'
        self.__cooling_pump = 'on'
        self.__cooling_fan = 'on'
        self.__fan = 'on'
        self.__fogging = 'on'
        self.__heating = 'on'
        self.__co2 = 'on'
        self.__lighting_1 = 'on'
        self.__lighting_2 = 'on'

    def get_roof_vent_south(self):
        return self.__roof_vent_south


    def get_roof_vent_north(self):
        return self.__roof_vent_north


    def get_side_vent(self):
        return self.__side_vent


    def get_shade_screen_north(self):
        return self.__shade_screen_north


    def get_shade_screen_south(self):
        return self.__shade_screen_south


    def get_thermal_screen(self):
        return self.__thermal_screen


    def get_cooling_pump(self):
        return self.__cooling_pump


    def get_cooling_fan(self):
        return self.__cooling_fan


    def get_fan(self):
        return self.__fan


    def get_fogging(self):
        return self.__fogging


    def get_heating(self):
        return self.__heating


    def get_co2(self):
        return self.__co2


    def get_lighting_1(self):
        return self.__lighting_1


    def get_lighting_2(self):
        return self.__lighting_2


    def get_shade_screen_out(self):
        return self.__shade_screen_out


    def get_shade_screen_in(self):
        return self.__shade_screen_in


    def get_irrigation(self):
        return self.__irrigation

    def get_update_time(self):
        return self.__update_time

    def set_update_time(self, value):
        self.__update_time = value

    def set_roof_vent_south(self, value):
        self.__roof_vent_south = value


    def set_roof_vent_north(self, value):
        self.__roof_vent_north = value


    def set_side_vent(self, value):
        self.__side_vent = value


    def set_shade_screen_north(self, value):
        self.__shade_screen_north = value


    def set_shade_screen_south(self, value):
        self.__shade_screen_south = value


    def set_thermal_screen(self, value):
        self.__thermal_screen = value


    def set_cooling_pump(self, value):
        self.__cooling_pump = value


    def set_cooling_fan(self, value):
        self.__cooling_fan = value


    def set_fan(self, value):
        self.__fan = value


    def set_fogging(self, value):
        self.__fogging = value


    def set_heating(self, value):
        self.__heating = value


    def set_co2(self, value):
        self.__co2 = value


    def set_lighting_1(self, value):
        self.__lighting_1 = value

    def set_lighting_2(self, value):
        self.__lighting_2 = value

    def handle_post(self, data):
        obj = json.loads(data)
        keys = obj.keys()
        json_response = "{"
        for key in keys:
            if key in Control.CONSTANT.tri_states_actuators:
                value = obj.get(key)
                if value in Control.CONSTANT.tri_states:
                    setattr(self, "_Control__" + key, value)
                    print key, getattr(self, "_Control__" + key)
                    json_response += '''"%s" : "%s",''' % (key, value)
                else:
                    print value, "illegal state"
            elif key in Control.CONSTANT.bi_states_actuators:
                value = obj.get(key)
                if value in Control.CONSTANT.bi_states:
                    setattr(self, "_Control__" + key, value)
                    print key, getattr(self, "_Control__" + key)
                    json_response += '''"%s" : "%s", ''' % (key, value)
                else:
                    print value, "illegal state"
            else:
                print key, "illegal actuator"
        json_response += '''"status" : "%s", ''' % "success"
        json_response += '''"update_time" : "%s"''' % get_current_time()
        json_response += "}"
        return json_response

    def build_json(self):
        return '''
        {
        "update_time": "%s",
        "actuator": {
            "tri_state": {
                "roof_vent_south": "%s",
                "roof_vent_north": "%s",
                "side_vent": "%s",
                "shade_screen_north": "%s",
                "shade_screen_south": "%s",
                "thermal_screen": "%s"
            },
            "bi_state": {
                "cooling_pump": "%s",
                "cooling_fan":"%s",
                "fan":"%s",
                "fogging": "%s",
                "heating": "%s",
                "co2": "%s",
                "lighting_1": "%s",
                "lighting_2": "%s"
                    }
                }
            }''' \
               % (  self.__update_time,
                    self.__roof_vent_south,
                    self.__roof_vent_north,
                    self.__side_vent,
                    self.__shade_screen_north,
                    self.__shade_screen_south,
                    self.__thermal_screen,
                    self.__cooling_pump,
                    self.__cooling_fan,
                    self.__fan,
                    self.__fogging,
                    self.__heating,
                    self.__co2,
                    self.__lighting_1,
                    self.__lighting_2
        )


if __name__ == '__main__':
    c = Control()
    # print c.build_json()
    c.set_co2(100)
    print c.build_json()
