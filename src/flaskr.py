from flask import Flask, session, request, json as flask_json
from flask_socketio import SocketIO, send, emit, join_room, leave_room, \
    Namespace

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this-is-secret'
socketio = SocketIO(app)

disconnected = None


@socketio.on('connect')
def on_connect():
    send('connected')
    send(json.dumps(dict(request.args)))
    send(json.dumps({h: request.headers[h] for h in request.headers.keys()
                     if h not in ['Host', 'Content-Type', 'Content-Length']}))


@socketio.on('disconnect')
def on_disconnect():


global disconnected
disconnected = '/'


@socketio.on('connect', namespace='/test')
def on_connect_test():


send('connected-test')
send(json.dumps(dict(request.args)))
send(json.dumps({h: request.headers[h] for h in request.headers.keys()
                 if h not in ['Host', 'Content-Type', 'Content-Length']}))


@socketio.on('disconnect', namespace='/test')
def on_disconnect_test():
    global disconnected
    disconnected = '/test'


@socketio.on('message')
def on_message(message):
    send(message)
    if message == 'test session':
        session['a'] = 'b'
    if message not in "test noackargs":
        return message


@socketio.on('json')
def on_json(data):
    send(data, json=True, broadcast=True)
    if not data.get('noackargs'):
        return data


@socketio.on('message', namespace='/test')
def on_message_test(message):
    send(message)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
