# coding=utf-8

from currenttime import get_current_time
from flask import Flask, request, Response
from outdoor import Outdoor
from control import Control
from scheduler import Scheduler
from indoor import Indoor
from control_command import ControlCommand
from werkzeug.contrib.fixers import ProxyFix

from database import get_db_indoor, get_db_outdoor, get_db_control_state, save_db_control_state, save_db_indoor, \
    save_db_outdoor, \
    get_db_control_command, save_db_control_command, handle_query_condition, handle_indoor_data, handle_outdoor_data

app = Flask(__name__)

node_num = 8
outdoor = Outdoor()
control = Control()
indoor = Indoor()
command = ControlCommand()
indoor_all_state = ''
web_control=False


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
    get_db_outdoor(outdoor)
    print 'outdoor updated', get_current_time()


def update_control():
    get_db_control_state(control)
    print 'control updated', get_current_time()


update_indoor()
update_outdoor()
update_control()
scheduler1 = Scheduler(300, update_outdoor)
scheduler2 = Scheduler(300, update_indoor)
# scheduler3 = Scheduler(10, update_control)
scheduler1.start()
scheduler2.start()
# scheduler3.start()

@app.route('/')
def arm_connect():
    return 'success'

@app.route('/indoor', methods=['GET', 'POST'])
def indoor_response():
    if request.method == 'GET':
        update_indoor()
        rsp = Response(indoor_all_state)
        rsp.headers['Access-Control-Allow-Origin'] = '*'
        return rsp
    elif request.method == 'POST':
        data = request.data
        handle_indoor_data(data)
        return 'success'
    else:
        return 'data error'


@app.route('/outdoor', methods=['GET', 'POST'])
def outdoor_response():
    if request.method == 'GET':
        update_outdoor()
        rsp = Response(outdoor.build_json())
        rsp.headers['Access-Control-Allow-Origin'] = '*'
        return rsp
    elif request.method == 'POST':
        data = request.data
        handle_outdoor_data(data)
        return 'success'
    else:
        print 'data error'


@app.route('/series', methods=['GET', 'POST', 'OPTIONS'])
def series_response():
    if request.method == 'POST':
        try:
            data = request.data
            response = handle_query_condition(data)
            rsp = Response(response)
            rsp.headers["Content-Type"] = ["text/html; charset=UTF-8"]
            rsp.headers['Access-Control-Allow-Origin'] = '*'
            rsp.headers['Access-Control-Allow-Methods'] = 'GET,POST,OPTIONS'
            rsp.headers['Access-Control-Allow-Headers'] = 'X-Requested-With, Content-Type'
            return rsp
        except ValueError:
            return ""
    if request.method == 'GET':
        return indoor_response()


@app.route('/control', methods=['GET', 'POST', 'OPTIONS'])
def control_response():
    global web_control,command
    if request.method == 'POST':
        try:
            data = request.data
            rsp = Response(control.handle_post(data))
            save_db_control_state(control)
            command.handle_post(data,isNumber=False)
            save_db_control_command(command)
            web_control=True
            rsp.headers["Content-Type"] = ["text/html; charset=UTF-8"]
            rsp.headers['Access-Control-Allow-Origin'] = '*'
            rsp.headers['Access-Control-Allow-Methods'] = 'GET,POST,OPTIONS'
            rsp.headers['Access-Control-Allow-Headers'] = 'X-Requested-With, Content-Type'
            return rsp
        except ValueError:
            return ""
    if request.method == 'GET':
        update_control()
        rsp = Response(control.build_json())
        rsp.headers["Content-Type"] = "text/html; charset=UTF-8"
        rsp.headers['Access-Control-Allow-Origin'] = '*'
        rsp.headers['Access-Control-Allow-Methods'] = 'GET,POST,OPTIONS'
        rsp.headers['Access-Control-Allow-Headers'] = 'X-Requested-With, Content-Type'
        return rsp
    else:
        rsp = Response("")
        rsp.headers["Content-Type"] = ["text/html; charset=UTF-8"]
        rsp.headers['Access-Control-Allow-Origin'] = '*'
        rsp.headers['Access-Control-Allow-Methods'] = 'GET,POST,OPTIONS'
        rsp.headers['Access-Control-Allow-Headers'] = 'X-Requested-With, Content-Type'
        return rsp

@app.route('/webControl')
def web_control():
    global web_control
    if web_control:
        web_control=False
        return command.build_control_command()
    else:
        return 'wait'

if __name__ == '__main__':
    app.run('0.0.0.0', 8050, threaded=True)
    # scheduler1.stop()
    # scheduler2.stop()
    # scheduler3.stop()
