from flask import Flask
import socket

app = Flask(__name__)



@app.route('/')
def hello():
    myHostName = socket.gethostname()
    return 'Hello from container {}'.format(myHostName)