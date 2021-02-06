import eventlet
import socketio

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})


@sio.event
def connect(sid, environ):
    print('connect ', sid)


@sio.event
def message(sid, data):
    print('message', sid, data)
    sio.emit('client1', "Hello world! from client 1")
    sio.emit('client2', "Hello world! from client 2")


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
