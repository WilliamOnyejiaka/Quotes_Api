from flask import Blueprint,jsonify,request
from pymongo import MongoClient
from src.config import MONGODB_URI
import json
from src.modules.Serializer import Serializer

crd = Blueprint('crd',__name__,url_prefix="/api/v1/quotes")
client = MongoClient(MONGODB_URI)
db = client.quotes_db.db

@crd.post('/<key>')
def quote(key):
    try:
        key = int(key)
    except:
        return jsonify({'error':True,'message':"key must be an integer from 1-102"}),400

    query = db.find_one({'key':key})
    if query:
        result = Serializer(['_id','quote','author','key']).serialize(query)
        return jsonify({'error':False,'item':result}),200

    return jsonify({'error':False,'message':"key must be an integer from 1-102"}),404