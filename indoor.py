class Indoor:
    '''the object of indoor climate'''

    def __init__(self, name='1'):
        self.__name = name
        self.__update_time = "2016/07/27 22:15:00"
        self.__temperature = "5"
        self.__humidity = "60"
        self.__radiation = "500"
        self.__co2 = "400"

    def set_name(self, value):
        self.__name = value

    def set_update_time(self, value):
        self.__update_time = value

    def set_temperature(self, temperature):
        self.__temperature = temperature

    def set_humidity(self, hum):
        self.__humidity = hum

    def set_radiation(self, rad):
        self.__radiation = rad

    def set_co2(self, co2):
        self.__co2 = co2

    def get_name(self):
        return self.__name

    def get_temperature(self):
        return self.__temperature

    def get_update_time(self):
        return self.__update_time

    def get_humidity(self):
        return self.__humidity

    def get_radiation(self):
        return self.__radiation

    def get_co2(self):
        return self.__co2

    def build_json(self):
        return '''
        {
           "indoor":{
               "%s":{
                    "temperature": "%s",
                    "humidity": "%s",
                    "radiation": "%s",
                    "co2": "%s",
                    "update_time": "%s"
                }
            }
        }''' \
               % (self.__name, self.__temperature, self.__humidity, self.__radiation,
                  self.__co2, self.__update_time)

    def build_json_array(self):
        return '''
               "%s":{
                    "temperature": "%s",
                    "humidity": "%s",
                    "radiation": "%s",
                    "co2": "%s",
                    "update_time": "%s"
                }''' \
               % (self.__name, self.__temperature, self.__humidity, self.__radiation,
                  self.__co2, self.__update_time)


if __name__ == '__main__':
    c = Indoor('2')
    print c.build_json()
    c.set_co2(100)
    print c.build_json_array()