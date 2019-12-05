

class FileIO:
    __actionIDDictioanry= {}

    def readAll(self, fileName):
        fileOpen = ""
        try:
            fileOpen = open(fileName,"r+")
        except IOError:
            print("IO error")
        line= fileOpen.readline().strip()
        while line != "":
            data = line.split(" ")
            if (len(data) > 1):  # data size is atleast 2
                self.__actionIDDictioanry[data[0]]= data[1]  #inserting to dictioanry
            line= fileOpen.readline()

        fileOpen.close()
        return self.__actionIDDictioanry # return all (action,id) pairs

    def append(self,fileName, newLine):
        fileOpen = ""
        try:
            fileOpen = open(fileName, "a")

        except IOError:
            print("IO error")
        newLine= newLine+"\n"
        fileOpen.write(newLine)
        fileOpen.close()
    def getActionIDDictionary(self):
        return self.__actionIDDictioanry


