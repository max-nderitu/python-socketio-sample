import socketio

sio = socketio.Client()


@sio.event
def connect():
    print('connection established')


@sio.event
def client1(data):
    print('client1 message received with ', data)


@sio.event
def disconnect():
    print('disconnected from server')


sio.connect('http://localhost:5000')
sio.wait()
