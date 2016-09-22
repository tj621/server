'''
Created on 2016/06/20

@author: Zxh
'''
from indoor import Indoor
from outdoor import Outdoor
from control import Control
from parameter import Parameter
from autorun import auto_run_main
from currenttime import get_time

node0 = Indoor('node0')
o = Outdoor()
c = Control()
p = Parameter()

p.set_expect_humidity("80")
p.set_humidity_influence_range_of_air_temperature("5")
p.set_high_humidity_influence_on_air_temperature("3")
p.set_low_humidity_influence_on_air_temperature("4")
p.set_light_influence_on_air_temperature_slope("0.7")

p.set_roof_vent_open_time("10")
p.set_shade_screen_in_time("5")
p.set_shade_screen_out_time("7")
p.set_side_vent_time("9")

start_time = get_time()
auto_run_main(node0, o, c, p)

