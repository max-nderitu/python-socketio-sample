import socketio

sio = socketio.Client()
sio.connect('http://localhost:5000')

print('my sid is', sio.sid)


@sio.event
def connect():
    print('Emitting messages...')

    sio.emit('message', "Hello world! from all")

    print('Emitted messages')

