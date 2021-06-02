import os
from flask import *

from datetime import datetime
import uuid
from controller.controller import FirebaseController
from database.database import DatabaseHelper
from file_mapping.FileIO import FileIO
from web_scraping.WebScraping import WebScraping

appController= FirebaseController()
file= FileIO()
actionIDMapContainer= file.readAll("ids.txt") # keep records of action - id

webSearch= WebScraping()


def isActionExist(actionIDs, action):
    if action in actionIDs:
        return True
    return False

def getID(action,actionIDs):
    return actionIDs[action]
def generateUniqueID():
    return str(uuid.uuid4())
def replaceChar(str):
    return str.replace('_', ' ')


"""flark """
app= Flask(__name__)


@app.route('/webhook', methods= ['GET', 'POST'])
def webhook():

    req = request.get_json(silent= True , force = True)
    action= req.get("queryResult").get("action") # action data from api.ai request to webhook
    if (isActionExist(actionIDMapContainer,action)):
        print("action exist")
        id= actionIDMapContainer[action]
        print(appController.webhookResponse(id).get('fulfillmentText'))
        return make_response(jsonify(appController.webhookResponse(id)))
    else:
        print("action not exist")
        ID = generateUniqueID().strip()
        actionIDMapContainer[action] = ID
        newLine = str(action) + " " + ID

        file.append("ids.txt", newLine.strip())
        searchKey= replaceChar(action)
        print(searchKey)
        searchKey = searchKey+ " iyte"
        text = webSearch.searchData(searchKey) #searcging for iyte
        print(text.getTextData())
        appController.sendDataToDatabase(ID, text)
        return make_response(jsonify({'fulfillmentText': text.getTextData()+ "\n" + text.getUrl()}))  







if __name__ == '__main__':
    port = int(os.getenv('PORT', 4000))
    app.run(port= port , host= '127.0.0.1')