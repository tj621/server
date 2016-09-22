'''

@author: Zxh
'''
from flask import Flask, g
import MySQLdb
from currenttime import get_current_time,make_time,stamp_for_series_start_time
from indoor import Indoor
from outdoor import Outdoor
from control import Control
import json


app = Flask(__name__)

# indooor_node_
#outdoor
#control_state
#control_command
#in_state

control_command_database = 'control_command'


def connect_db():
    """Connects to the specific database."""
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="greenhouse")
    db.autocommit(True)
    return db


def get_db():
    if not hasattr(g, 'mysql_db'):
        g.mysql_db = connect_db()
    return g.mysql_db


def save_db_control_command(CommandControl):
    with app.app_context():
        db = get_db()
        db.cursor().execute(
            'insert into ' + control_command_database + '(update_time,control_actutator,control_cmd) values(%s,%s,%s)',
            [get_current_time(), CommandControl.get_actutator(), CommandControl.get_command()])
        db.commit()
        db.cursor().close()
        db.close()
    print 'control command save success'


def get_db_control_command(CommandControl):
    sheet_name = control_command_database
    query = "SELECT * FROM " + sheet_name + " WHERE id=(select max(id) from " + sheet_name + ")"
    row = query_db(query)
    CommandControl.set_update_time(row[1])
    CommandControl.set_actutator(row[2])
    CommandControl.set_command(row[3])


def save_db_indoor(Indoor):
    with app.app_context():
        db = get_db()
        indoor_node = "indoor_node_" + Indoor.get_name()
        db.cursor().execute(
            'insert into ' + indoor_node + '(node,update_time,temperature,humidity,radiation,co2) values(%s,%s,%s,%s,%s,%s)',
            [Indoor.get_name(), get_current_time(), Indoor.get_temperature(), Indoor.get_humidity(),
             Indoor.get_radiation(), Indoor.get_co2()])
        db.commit()
        db.cursor().close()
        db.close()
    print 'indoor save success'


def get_db_indoor(Indoor):
    sheet_name = 'indoor_node_' + str(Indoor.get_name())
    query = "SELECT * FROM " + sheet_name + " WHERE id=(select max(id) from " + sheet_name + ")"
    row = query_db(query)
    Indoor.set_name(row[1])
    Indoor.set_update_time(row[2])
    Indoor.set_temperature(row[3])
    Indoor.set_humidity(row[4])
    Indoor.set_radiation(row[6])
    Indoor.set_co2(row[6])


#    return Indoor.build_json()


def save_db_outdoor(Outdoor):
    with app.app_context():
        db = get_db()
        db.cursor().execute('insert into outdoor(update_time,temperature,humidity,radiation,co2,wind_direction,wind_speed,rain_snow,atmosphere)\
                   values(%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                            [Outdoor.get_update_time(), Outdoor.get_temperature(), Outdoor.get_humidity(),
                             Outdoor.get_radiation(), Outdoor.get_co_2(),
                             Outdoor.get_wind_direction(), Outdoor.get_wind_speed(), Outdoor.get_rain(),
                             Outdoor.get_atmosphere()])
        db.commit()
    print 'outdoor save success'


def get_db_outdoor(Outdoor):
    query = "select * from outdoor where id=(select max(id) from outdoor)"
    row = query_db(query)
    Outdoor.set_update_time(row[1])
    Outdoor.set_temperature(row[2])
    Outdoor.set_humidity(row[3])
    Outdoor.set_radiation(row[4])
    Outdoor.set_co_2(row[5])
    Outdoor.set_wind_direction(Outdoor.wind_direction_data.get(str(row[6])))
    Outdoor.set_wind_speed(row[7])
    Outdoor.set_rain(row[8])
    Outdoor.set_atmosphere(row[9])


#    return Outdoor.build_json()

def save_db_control_state(Control):
    with app.app_context():
        db = get_db()
        db.cursor().execute('insert into control_state(update_time,roof_vent_south,roof_vent_north,side_vent,shade_screen_north,shade_screen_south,thermal_screen,\
        cooling_pump,cooling_fan,fan,fogging,heating,co2,lighting_1,lighting_2) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                            [get_current_time(), Control.get_roof_vent_south(), Control.get_roof_vent_north(),
                             Control.get_side_vent(), Control.get_shade_screen_north(),
                             Control.get_shade_screen_south(), Control.get_thermal_screen(),
                             Control.get_cooling_pump(), Control.get_cooling_fan(), Control.get_fan(),
                             Control.get_fogging(),
                             Control.get_heating(), Control.get_co2(), Control.get_lighting_1(),
                             Control.get_lighting_2()])
        db.commit()
        db.cursor().close()
        db.close()
    print 'control save success'


def get_db_control_state(Control):
    query = 'select * from control_state where id=(select max(id) from control_state)'
    row = query_db(query)
    Control.set_update_time(row[1])
    Control.set_roof_vent_south(row[2])
    Control.set_roof_vent_north(row[3])
    Control.set_side_vent(row[4])
    Control.set_shade_screen_north(row[5])
    Control.set_shade_screen_south(row[6])
    Control.set_thermal_screen(row[7])
    Control.set_cooling_pump(row[8])
    Control.set_cooling_fan(row[9])
    Control.set_fan(row[10])
    Control.set_fogging(row[11])
    Control.set_heating(row[12])
    Control.set_co2(row[13])
    Control.set_lighting_1(row[14])
    Control.set_lighting_2(row[15])


#get one row
def query_db(query, args=(), one=False):
    with app.app_context():
        cur = get_db().cursor()
        count = cur.execute(query)
        # print count
        result = cur.fetchone()
        cur.close()
        get_db().close()
        return result

#get all rows
def query_db_2(query, args=(), one=False):
    with app.app_context():
        cur = get_db().cursor()
        count = cur.execute(query)
        # print count
        result = cur.fetchall()
        cur.close()
        get_db().close()
        return result

#get property column number


def handle_query_condition(request_data):
    obj = json.loads(request_data)
    keys = obj.keys()
    start_time=make_time(obj.get('start'),0)
    end_time=make_time(obj.get('stop'),1)
    if(end_time>get_current_time()):
        end_time=get_current_time()
    response_data='''{"series":['''
    for key in keys:
        value=obj.get(key)
        if(value=='true'):
            data=key.split('_')
            if(data[0][1]=='n'):
                sheet_name = 'indoor_node_'+data[0][4]
            else: sheet_name = 'outdoor'
            sheet_title = "update_time,"+data[1]
            query = "SELECT "+sheet_title+" FROM " +sheet_name+ " WHERE update_time BETWEEN "+"'" +start_time+"'" +" AND "+"'" +end_time+"'"
            rows = query_db_2(query)
            data='''['''
            for row in rows:
                temp ='''[%s,%s]'''% (stamp_for_series_start_time(str(row[0])),float(row[1]))
                data += temp
                data += ','
            data_list=list(data)
            data_list.pop()
            data = "".join(data_list)
            data = "]"
            response_data += '''{
                "name":"%s",
                "data":%s,
                "pointStart":%s,
                "pointInterval": "5 * 60 * 1000"
                },
                ''' % (key,data,stamp_for_series_start_time(start_time))
    response_data+='''{}
                    ]}'''
    return response_data

# def get_db_actutor_current_state():
#     #global c,co
#     query = 'select * from in_state where id=(select max(id) from in_state)'
#     a = query_db(query)
#     row =[]
#     for i in a:
#         row.append(i)
#     print row
#     return '''
#     {
#         "update_time": "%s",
#         "actuator": {
#             "tri_state": {
#                 "roof_vent_south": "%s",
#                 "roof_vent_north": "%s",
#                 "side_vent": "%s",
#                 "shade_screen_north": "%s",
#                 "shade_screen_south": "%s",
#                 "thermal_screen": "%s"
#             },
#             "bi_state": {
#                 "cooling_pump": "%s",
#                 "cooling_fan": "%s",
#                 "fan": "%s",
#                 "fogging": "%s",
#                 "heating": "%s",
#                 "co2": "%s",
#                 "lighting_1": "%s",
#                 "lighting_2": "%s"
#             }
#         }
#     }
#     '''%(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15])



if __name__ == '__main__':
    print 'test start'
    indoor = Indoor('2')
    outdoor = Outdoor()
    control = Control()
    # print get_db_actutor_current_state()
    #d='''{"outdoor_radiation": "true","start": "2016-06-17",
    #"stop": "2016-08-22"}'''
    #print handle_query_condition(d)
    outdoor.get_weather_from_api()
    #save_db_outdoor(outdoor)
    # print outdoor.build_json()
    # temperature, humidity, radiation, co2, wind_direction, wind_speed, rain_snow,atmosphere
    print outdoor.get_wind_direction()
    outdoor.set_wind_direction_number()
    print outdoor.get_wind_direction()
    # print outdoor.get_rain()
    with app.app_context():
        db = get_db()
        db.cursor().execute('insert into outdoor(wind_direction)\
                   values(%s)',
                            [outdoor.get_wind_direction()])
        db.commit()
    # query = 'select * from control_state where id=(select max(id) from control_state)'
    # query_db(query)
    # get_db_control_state(control)
    # print control.build_json()
    # get_db_indoor(indoor)
    # print indoor.build_json()
    # get_db_outdoor(outdoor)
    # print outdoor.build_json()
    # save_db_control_state(control)
    # save_db_indoor(indoor)
    # save_db_outdoor(outdoor)
    # init_db()
