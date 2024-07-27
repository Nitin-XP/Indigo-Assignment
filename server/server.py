from bson import ObjectId
from flask import Flask, jsonify  # type: ignore
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)

#MongoDB Connection
client = MongoClient("mongodb+srv://extravagant150103:C2pwAndfWi5qAqTm@indigo.td0lwab.mongodb.net/?retryWrites=true&w=majority&appName=Indigo")
db = client['indigo']

# FlightData reading
flightCollection = db['flightData']
flightData = flightCollection.find()

def mongo_to_dict(doc):
    return {key: str(value) if isinstance(value, ObjectId) else value for key, value in doc.items()}

flightDataList = [mongo_to_dict(doc) for doc in flightData]

CORS(app, origins=["http://localhost:5173"])
@app.route("/flightData", methods=['GET'])
def flightInfo():
    return flightDataList

if __name__ == "__main__":
    app.run(debug=True)