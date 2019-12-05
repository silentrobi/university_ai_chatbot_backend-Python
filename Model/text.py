class Text:
    __textData=""
    __url=""

    def __init__(self, textData, url):
        self.__textData=textData
        self.__url=url

    def setTextData(self, textData):
        if (textData != str):
            print("Input should be  String")
        else:
            self.__textData=textData
    def setUrl(self,url):
        if (url != str):
            print("Input should be  String")
        else:
            self.__url=url

    def getTextData(self):
        return self.__textData
    def getUrl(self):
        return self.__url
