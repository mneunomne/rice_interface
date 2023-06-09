import socketio

global socketClient
is_connected = False

def connectSocket(server_path):
    try:
        socketClient = socketio.Client()
        socketClient.connect(server_path)
    except socketio.exceptions.ConnectionError as err:
        is_connected = False
        print("Error on socket connection")
    else:
        is_connected = True

def sendData (textSound):
    try:
        socketClient.emit('test', 'moin')
    except socketio.exceptions.BadNamespaceError as err:
        print("error sending data", err)
