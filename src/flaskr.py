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


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
