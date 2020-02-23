from pymongo import MongoClient
import pymongo

client = pymongo.MongoClient("mongodb+srv://react:react@malya-gso2y.mongodb.net/test?retryWrites=true&w=majority/")

db = client.Election_Data

def state_names():
    collection = db.Election_Result
    teams = collection.distinct('State')
    return [t for t in teams]

def constituency_names(state):
    collection = db.Election_Result
    constitu = collection.find({"State": state} , {"_id":0,"Constituency":1})
    re = []
    for r in constitu:
        if r['Constituency'] in re:
            pass
        else:
            re.append(r['Constituency'])
    return re

def getConstituencyDetails(state,constitu):
    collection = db.Election_Result
    res = collection.find({"State": state , "Constituency" : constitu},{"_id":0})
    return [r for r in res]
    
def get_winner_name(state,constitu):
    collection = db.Win_Stats
    res = collection.find({"State": state , "Constituency" : constitu},{"_id":0 , "Candidate":1})
    return [r for r in res]

    

