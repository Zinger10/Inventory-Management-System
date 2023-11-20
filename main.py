from flask import jsonify
from website import create_app
from website import db 

from flask import Flask
from sqlalchemy import text

app = create_app()

if __name__ == '__main__':
    app.run( host='192.168.0.104', debug = 'True')


#Trying to change in github to check in remote server