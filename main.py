# coding=utf-8

from currenttime import get_current_time
from flask import Flask, request,Response
from outdoor import Outdoor
from control import Control
from scheduler import Scheduler
from indoor import Indoor
from control_command import ControlCommand

from database import get_db_indoor, get_db_outdoor, get_db_control_state, save_db_control_state, save_db_indoor, \
    save_db_outdoor, \
    get_db_control_command, save_db_control_command ,handle_query_condition



app = Flask(__name__)

node_num = 8
outdoor = Outdoor()
control = Control()
indoor = Indoor()
command = ControlCommand()
indoor_all_state = ''
outdoor_state=''

def update_indoor():
    global indoor_all_state
    number = node_num
    get_db_indoor(indoor)
    indoor_all_state = '''{''' + indoor.build_json_array()
    for i in range(number - 1):
        temp = Indoor(str(i + 2))
        indoor_all_state += ','
        get_db_indoor(temp)
        indoor_all_state += temp.build_json_array()
    indoor_all_state += '''}'''
    print 'indoor update', get_current_time()


def update_outdoor():
    global outdoor_state
    try:
        outdoor.get_weather_from_api()
        outdoor.set_wind_direction_number()
        save_db_outdoor(outdoor)
    except:
        print "get outdoor information error"
    finally:
        get_db_outdoor(outdoor)
    outdoor_state=outdoor.build_json()
    print 'outdoor updated', get_current_time()


def update_control():
    get_db_control_state(control)
    print 'control updated', get_current_time()


update_indoor()
update_outdoor()
update_control()

scheduler2 = Scheduler(300, update_outdoor)
#scheduler3 = Scheduler(300, update_indoor)
#scheduler4 = Scheduler(300, update_control)
scheduler2.start()
#scheduler3.start()
#scheduler4.start()


@app.route('/indoor')
def indoor_response():
    update_indoor()
    rsp = Response(indoor_all_state)
    rsp.headers['Access-Control-Allow-Origin'] = '*'
    #rsp.headers['Connection'] = "Keep-Alive"
    return rsp


@app.route('/outdoor')
def outdoor_response():
    update_outdoor()
    #rsp = Response(outdoor.build_json())
    rsp = Response(outdoor_state)
    #rsp.headers['Connection'] = "Keep-Alive"
    rsp.headers['Access-Control-Allow-Origin'] = '*'
    return rsp


@app.route('/control', methods=['GET', 'POST' , 'OPTIONS'])
def control_response():
    if request.method == 'POST':
        print "post"
        try:
            data = request.data
            rsp = Response(control.handle_post(data))
            save_db_control_state(control)
            command.handle_post(data)
            save_db_control_command(command)
            rsp.headers["Content-Type"] = "text/html; charset=UTF-8"
            rsp.headers['Access-Control-Allow-Origin'] = '*'
            rsp.headers['Access-Control-Allow-Methods'] = 'GET,POST,OPTIONS'
            rsp.headers['Access-Control-Allow-Headers'] = 'X-Requested-With, Content-Type'
            return rsp
        except ValueError:
            return "actutor error, please review"
    elif request.method == 'GET':
        update_control()
        rsp = Response(control.build_json())
        rsp.headers["Content-Type"] = "text/html; charset=UTF-8"
        rsp.headers['Access-Control-Allow-Origin'] = '*'
        rsp.headers['Access-Control-Allow-Methods'] = 'GET,POST,OPTIONS'
        rsp.headers['Access-Control-Allow-Headers'] = 'X-Requested-With, Content-Type'
        return rsp
    else:
        print "options"
        rsp = Response("")
        rsp.headers["Content-Type"] = "text/html; charset=UTF-8"
        rsp.headers['Access-Control-Allow-Origin'] = '*'
        rsp.headers['Access-Control-Allow-Methods'] = 'GET,POST,OPTIONS'
        rsp.headers['Access-Control-Allow-Headers'] = 'X-Requested-With, Content-Type'
        return rsp


@app.route('/series',methods=['GET', 'POST' , 'OPTIONS'])
def series_response():
    if request.method == 'POST':
        try:
            data = request.data
            response_data = handle_query_condition(data)
            rsp = Response(response_data)
            rsp.headers["Content-Type"] = "text/html; charset=UTF-8"
            rsp.headers['Access-Control-Allow-Origin'] = '*'
            rsp.headers['Access-Control-Allow-Methods'] = 'GET,POST,OPTIONS'
            rsp.headers['Access-Control-Allow-Headers'] = 'X-Requested-With, Content-Type'
            return rsp
        except ValueError:
            return "something wrong : you post nothoing"
    else:
        rsp = Response("")
        rsp.headers["Content-Type"] = "text/html; charset=UTF-8"
        rsp.headers['Access-Control-Allow-Origin'] = '*'
        rsp.headers['Access-Control-Allow-Methods'] = 'GET,POST,OPTIONS'
        rsp.headers['Access-Control-Allow-Headers'] = 'X-Requested-With, Content-Type'
        return rsp



if __name__ == '__main__':
    app.run('0.0.0.0', 8020,threaded=True)
    scheduler2.stop()
    scheduler3.stop()
    #print 'I am dieing when time is ',get_current_time()
   
