from crypt import methods
from flask import Flask, render_template, request, jsonify
import json
import pymongo
from pymongo import MongoClient
from datetime import datetime

app=Flask(__name__)

def get_db():
    client = MongoClient(host='test_mongodb',
                         port=27017, 
                         username='root', 
                         password='pass',
                        authSource="admin")
    db = client["amazon_db"]
    return db

@app.route('/')
def ping_server():
    return "Welcome to the Amazon Query."

@app.route('/to_query', methods=['POST','GET'])
def index():    
    if request.method=='POST':
        amazon_rating=request.from['Rating']
        amazon_product=request.from['Product']
        db=""
        try:
            db = get_db()
            query_5 = { 
            "rating": { 
                "$gte": amazon_rating
            },
            "itemName": {
                "$regex": amazon_product,
                "$options": "i"
            }
            }                
            _amazons = db.amazon_tb.find(query_5)
            amazons = [{ "name": amazon["name"],"price": amazon["price"], "rating": amazon["rating"]} for amazon in _amazons]
            return jsonify({"amazons": amazons})        
    else:
        return render_template('index.html')



if __name__=="__main__":
    app.run(debug=True)
    