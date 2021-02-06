# python-socketio-sample
This is a sample implementation of the python socketio implementation  

## How to run the application
### Install all the required dependencies in Pipfile via 
`pipenv install`

### First start up the server
`pipenv run python server.py`

### Then run the clients on other terminal tabs 
`pipenv run python client1.py`
`pipenv run python client2.py`

### Then run the emit script and monitor the messages transmited 
`pipenv run python emit.py`

Messages should be logged as transmitted
