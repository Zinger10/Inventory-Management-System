from flask import jsonify
from website import create_app
from website import db 

from flask import Flask
from sqlalchemy import text

app = create_app()

if __name__ == '__main__':
    app.run(  debug = 'True', host = '192.168.0.100')


#Trying to change in github to check in remote server