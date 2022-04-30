from crypt import methods
import numpy as np
from flask import Flask, render_template, request, jsonify
import json
import pandas as pd
import numpy as np
import pymongo
from pymongo import MongoClient
from datetime import datetime
import sqlite3
import sqlalchemy

app=Flask(__name__)

engine = sqlalchemy.create_engine('sqlite:///amazon_search_history.db')
df_search.to_sql('search_history',engine,if_exists='replace',index=False)
df_search_sql=pd.read_sql('SELECT history_search',engine)


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
        # insert search data into SQL-databse
        engine.session.db(amazon_product)
        # return the results from mongodb_databse
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

# based on customers' searching history, then show the most popular searches
@app.route('/search_analysis')
def query_search():
    history_results=df_search_sql.sort_values('history_search').groupby('history_search').head()
    return history_results


if __name__=="__main__":
    app.run(debug=True)
    