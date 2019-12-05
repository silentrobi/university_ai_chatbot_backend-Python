import urllib
from bs4 import BeautifulSoup
from googlesearch import search
from Model.text import Text


class WebScraping:
   def searchData(self,query ):
      url= ""
      text= ""
      allText = ""
      for i in search(query=query,lang='en',num=1,stop= 1):
              url= i
              soup = None
              try:
                urlLoader= urllib.request.urlopen(i)
                html= urlLoader.read()
                soup = BeautifulSoup(html,"html.parser")
              except Exception as e:
                  print("Error occured to load the url!!")
                  allText = "Error occured to load the url!!"





              if (soup != None):
                  # kill all script and style elements
                for script in soup(["script", "style"]):
                  script.decompose()  # rip it out

                resutSet = soup.find_all('p')

                for tag in resutSet:
                  text = str(tag.get_text()).strip()
                  text = " ".join(text.split())  # remove white spaces
                  allText += text



      return Text(str(allText),str(url))

