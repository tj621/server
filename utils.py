# coding=utf-8
def control_response(method,data):
    if method == 'POST':
        try:

            rsp = Response(control.handle_post(data))
            save_db_control_state(control)
            command.handle_post(data)
            save_db_control_command(command)
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