# coding=utf-8
import json
from CONTROL_CONSTANT import CONTROL_CONSTANT


class ControlCommand():

    CONSTANT = CONTROL_CONSTANT()

    def __init__(self):
        self.__update_time = '2016/07/21 00:00:00'
        self.__actuator = 'roof_vent_south'
        self.__command = 'stop'

    def get_update_time(self):
        return self.__update_time

    def set_update_time(self, value):
        self.__update_time = value

    def get_actuator(self):
        return self.__actuator

    def set_actuator(self, value):
        self.__actuator = value

    def get_command(self):
        return self.__command

    def set_command(self, value):
        self.__command = value

    def get_actuator_number(self, key):
        return ControlCommand.CONSTANT.control_actuator_number.get(key)

    def get_actuator_name(self, value):
        for key in ControlCommand.CONSTANT.actuator:
            if ControlCommand.CONSTANT.control_actuator_number.get(key) == value:
                return key
        print 'actuator number value error'

    def get_cmd_number(self, key):
        if key in ControlCommand.CONSTANT.tri_states:
            return ControlCommand.CONSTANT.tri_states_control_cmd.get(key)
        elif key in ControlCommand.CONSTANT.bi_states_actuators:
            return  ControlCommand.CONSTANT.bi_states_control_cmd.get(key)
        else:
            return "key error : control status error"

    def get_cmd_status(self, value):
        tmp = False
        for key in ControlCommand.CONSTANT.bi_states:
            if ControlCommand.CONSTANT.bi_states_control_cmd.get(key) == value:
                return key
                tmp = True
        if(tmp == False):
            for key in ControlCommand.CONSTANT.tri_states_actuators:
                if ControlCommand.CONSTANT.tri_states_control_cmd.get(key) == value:
                    return key
        print 'cmd number value error'

    def handle_post(self, data,isNumber=True):
        obj = json.loads(data)
        keys = obj.keys()
        for key in keys:
            if isNumber:
                self.set_actuator(ControlCommand.CONSTANT.control_actuator_number.get(key))
                if key in ControlCommand.CONSTANT.tri_states_actuators:
                    value = obj.get(key)
                    if value in ControlCommand.CONSTANT.tri_states:
                        self.set_command(ControlCommand.CONSTANT.tri_states_control_cmd.get(value))
                    else:
                        print value, "illegal state"
                elif key in ControlCommand.CONSTANT.bi_states_actuators:
                    value = obj.get(key)
                    if value in ControlCommand.CONSTANT.bi_states:
                        self.set_command(ControlCommand.CONSTANT.bi_states_control_cmd.get(value))
                    else:
                        print value, "illegal state"
                else:
                    print key, "illegal actuator"
            else:
                self.set_actuator(key)
                self.set_command(obj.get(key))
    def build_json(self):
        return '''
                {
                  "update_time":"%s",
                  "actuator":"%s",
                  "command":"%s"
                }
        '''%(self.__update_time,self.__actuator,self.__command)
    def build_control_command(self):
        return '''
                {
                  "%s":"%s"
                }
        ''' % (self.__actuator, self.__command)

if __name__ == '__main__':
    c = ControlCommand()
    print c.get_actuator_name('1')
    print c.get_actuator_number('roof_vent_south')
    print c.get_cmd_number('on')
    print c.get_cmd_status('1')
