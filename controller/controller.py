
from database.database import DatabaseHelper
class FirebaseController:

    firebaseDatabaseHelper = DatabaseHelper()
    def webhookResponse(self, ID): #get data from firebase database
        ID= str(ID).strip()
        if (ID ==   ""):
            return {'fulfillmentText': 'error empty action'}  # if nothing is found

        data= self.firebaseDatabaseHelper.getQueryData(ID)
        return self.__formateDataForWebhook(data) # return json









    def __formateDataForWebhook(self, firebaseData):

        if(bool(firebaseData) == False): # if no data is found means dic is empty then return default answer
            return {'fulfillmentText': "We don't have answer of your query."}

        result= str(firebaseData.get("result"))
        url= str(firebaseData.get("url"))

        response= {'fulfillmentText': result+ "\n" + url}
        return response

    def sendDataToDatabase(self,ID, textObject):
        self.firebaseDatabaseHelper.insetQueryData(ID, textObject)






