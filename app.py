from flask import Flask,jsonify
from mongo_flask import MongoJSONEncoder
from flask_cors import CORS,cross_origin
import database as db

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'application/json'

@app.route('/')
def index():
    return jsonify({"message" : "API is Working"})

@app.route('/getStates')
def getStates():
    res = db.state_names()
    res.sort()
    return jsonify({"states":res})

@app.route('/getConstituency/<state>')
def getConstituency(state):
    res = db.constituency_names(state)
    return jsonify({"Constituency":res})

@app.route('/getConstDetails/<state>/<constitu>')
def getConstituencyDetails(state,constitu):
    res = db.getConstituencyDetails(state,constitu)
    return jsonify({"details":res})

@app.route ('/winner/<state>/<constitu>')
def getWinner(state,constitu):
    res = db.get_winner_name(state,constitu)
    return jsonify({"winner":res[0]["Candidate"]})

if __name__ == "__main__":
    app.run(debug = True , port=5050)