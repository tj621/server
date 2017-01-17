# coding=utf-8
import json
import urllib
from currenttime import get_current_time

url = 'https://api.heweather.com/x3/weather?city=jiading&key=8924d0a789dd4e348982cfe7f721267c'


class Outdoor(object):
    wind_direction_data={
        "1":u"东风",
        "2":u"南风",
        "3":u"西风",
        "4":u"北风",
        "12":u"东南风",
        "14":u"东北风",
        "23":u"西南风",
        "34":u"西北风"
    }

    def get_db_wind_direction(self, key):
        return self.wind_direction_data.get(key)

    def set_wind_direction_number(self):
        value = self.get_wind_direction()
        keys = self.wind_direction_data.keys()
        for key in keys:
            if self.wind_direction_data[key]==value:
                self.set_wind_direction(key)

    def __init__(self):
        self.__update_time = "just now"
        self.__temperature = 10.0
        self.__humidity = 5
        self.__radiation = 600
        self.__co2 = 600
        self.__wind_direction = "12"
        self.__wind_speed = 3
        self.__rain = 1
        self.__atmosphere = 0

    def get_update_time(self):
        return self.__update_time


    def get_temperature(self):
        return self.__temperature


    def get_humidity(self):
        return self.__humidity


    def get_radiation(self):
        return self.__radiation


    def get_co_2(self):
        return self.__co2


    def get_wind_direction(self):
        return self.__wind_direction


    def get_wind_speed(self):
        return self.__wind_speed


    def get_rain(self):
        return self.__rain


    def get_atmosphere(self):
        return self.__atmosphere

    def set_update_time(self, value):
        self.__update_time = value


    def set_temperature(self, value):
        self.__temperature = value


    def set_humidity(self, value):
        self.__humidity = value


    def set_radiation(self, value):
        self.__radiation = value


    def set_co_2(self, value):
        self.__co2 = value


    def set_wind_direction(self, value):
        self.__wind_direction = value


    def set_wind_speed(self, value):
        self.__wind_speed = value


    def set_rain(self, value):
        self.__rain = value


    def set_atmosphere(self, value):
        self.__atmosphere = value


    def set_outdoor(self, update_time1, temperature1, humidity1, radiation1, co21, wind_direction1, wind_speed1,
                    rain1, atmosphere1):
        self.__update_time = update_time1
        self.__temperature = temperature1
        self.__humidity = humidity1
        self.__radiation = radiation1
        self.__co2 = co21
        self.__wind_direction = wind_direction1
        self.__wind_speed = wind_speed1
        self.__rain = rain1
        self.__atmosphere = atmosphere1


    def build_json(self):
        return '''
        {
            "outdoor":{
                "temperature":"%s",
                "humidity":"%s",
                "radiation":"%s",
                "co2":"%s",
                "wind_direction":"%s",
                "wind_speed":"%s",
                "rain":"%s",
                "atmosphere":"%s",
                "update_time":"%s"
            }
        }''' \
               % (self.__temperature, self.__humidity, self.__radiation, self.__co2, self.__wind_direction,
                  self.__wind_speed, self.__rain, self.__atmosphere, self.__update_time)

    def get_weather_from_api(self):
        try:
            data = urllib.urlopen(url).read()
        except:
            print 'Internet error'
        wea_json = json.loads(data)
        wea_json = wea_json['HeWeather data service 3.0'][0]
        update_time = get_current_time()
        temperature = str(wea_json['now']['tmp'])
        humidity = str(wea_json['now']['hum'])
        radiation = '300'
        co2 = '600'
        wind_direction = wea_json['now']['wind']['dir']
        wind_speed = '%.1f' % (float(wea_json['now']['wind']['spd']) / 3.6)
        rain = wea_json['now']['pcpn']
        # if (float(rain)) > 1.0:
        #    rain = 'true'  # raining
        #else:
        #    rain = 'false'  # no rain
        atmosphere = str(wea_json['now']['pres'])
        self.set_outdoor(update_time, temperature, humidity, radiation, co2, wind_direction, wind_speed, rain,
                         atmosphere)


if __name__ == '__main__':
    print 'test'
    a = Outdoor()
    a.get_weather_from_api()
    print a.build_json()
    print a.get_wind_speed()