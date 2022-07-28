from flask import session
from extensions import sock


@sock.on('connect')
def connect():
    print('connected')
    print(session["user"])
