import pyrebase
class DatabaseHelper:
   __config = {
    "apiKey": "AIzaSyAIAD_5HVSzAJTJ8GEIBvKYocxoJyE8doQ",
    "authDomain": "chatwebhook.firebaseapp.com",
    "databaseURL": "https://chatwebhook.firebaseio.com",
    "projectId": "chatwebhook",
    "storageBucket": "chatwebhook.appspot.com",
    "messagingSenderId": "57715123999",
    "appId": "1:57715123999:web:2565a60823b31171"
  }

   def __init__(self):
        self.__db = pyrebase.initialize_app(self.__config).database()

   def getQueryData(self, ID):
       result= {}
       ID= ID.strip()
       try:
           result= self.__db.child("IYTE Database").child(ID).get().val()
           #print(result) #output check
       except Exception as e:
           return {"result": "Error occured during firebase data read operation\n"}
       return result
   def insetQueryData(self, ID, textObject):
       data={}
       data["result"] = textObject.getTextData()
       data["url"]= textObject.getUrl()
       try:
        self.__db.child("IYTE Database").child(ID).set(data)
       except Exception as e:
           print("Firebase data Insert error\n")

   def updateQueryData(self):
       return
   def delete(self):
       return








