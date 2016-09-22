# coding=utf-8
class CONTROL_CONSTANT():
    tri_states_actuators = ("roof_vent_south", "roof_vent_north", "side_vent", "shade_screen_north",
                            "shade_screen_south", "thermal_screen")
    bi_states_actuators = (
        "cooling_pump", "cooling_pad", "fogging", "heating", "co2", "lighting_1", "lighting_2", "irrigation")

    actutator = ("roof_vent_south", "roof_vent_north", "side_vent", "shade_screen_north", "cooling_pump", "cooling_pad",
                 "fogging", "heating", "co2", "lighting_1", "lighting_2", "irrigation", "shade_screen_south",
                 "thermal_screen")

    tri_states = ("on", "off", "stop")

    bi_states = ("on", "off")

    control_actutator_number = {
        'roof_vent_south': '1',
        'roof_vent_north': '2',
        'side_vent': '3',
        'shade_screen_south': '4',
        'shade_screen_north': '5',
        'thermal_screen': '6',
        'cooling_fan': '9',
        'cooling_pump': '10',
        'fan': '11',
        'heating': '12',
        'fogging': '13',
        'co2': '14',
        'lighting_1': '15',
        'lighting_2': '16'
    }

    tri_states_control_cmd = {
        'on': '1',
        'off': '2',
        'stop': '0'
    }

    bi_states_control_cmd={
        'on':'1',
        'off':'0'
    }


