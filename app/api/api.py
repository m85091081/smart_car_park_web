'''
@author:reimu

Blueprint for api
'''
from flask import Blueprint, jsonify, Response
from db import get_db
import pymongo
from .. import socketio

api = Blueprint('api', __name__)
park_db = get_db()

@api.route('/status/change', methods=['GET', 'POST'])
def register():
    '''register route'''
    status = park_db['Status']
    try:
        raw = {
            'park':'park0',
            'status':True
            }
        status.insert_one(raw)
    except pymongo.errors.DuplicateKeyError:
        return Response("{'message':'user already exist.','code':409}",
                        status=409,
                        mimetype='application/json')
    return jsonify({"code": 200, "message": "ok"})
