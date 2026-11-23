from flask_pymongo import PyMongo
from dotenv import load_dotenv
from flask import Flask,render_template,request
import os


load_dotenv()  # Load variables from .env and .flaskenv
db_user = os.getenv('MONGODB_USERNAME')
db_pass = os.getenv('MONGODB_PASSWORD')
print(db_user)

# THIS IS A WAY TO CONNECT TO MONGO DB USING FLASK AND PYTHON
uri = os.getenv("MONGODB_URI")
app = Flask(__name__)
# set a config var
app.config["MONGO_URI"] = uri
mongo = PyMongo(app)
try:
    #get details of the client
    print (mongo.cx)
    print("You successfully connected to MongoDB!")
except Exception as e:
    print(e)