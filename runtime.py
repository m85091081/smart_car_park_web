'''
@author:reimu

runtime for webserver
'''
from app import app_create, socketio
import db

app = app_create()

if __name__ == '__main__':
    db.init_db(db.get_db())
    socketio.run(app,host='0.0.0.0',port=8509)
