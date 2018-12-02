import urllib
import webbrowser
from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.request
import re


class Search:
    def __init__(self, searchIn = None, engineIn = "google", domainIn = "ca"):
        self.searchRaw = searchIn
        self.searchQuery = ""
        self.engine = engineIn
        self.domain = domainIn
        self.url = ""
        self.searchString = "/search?q="
    #end of constructor

    #set search engine
    def setEngine(self, engineIn):
        self.engine = engineIn
    #end of setEngine

    #set domain engine
    def setDomain(self, domainIn):
        self.domain = domainIn
    #end of setdomain
    
    #set search Query
    def setQuery(self, searchIn):
        self.searchRaw = searchIn
    #end of setQuery

    def buildLink(self):
        if self.engine == "amazon":
            self.searchString = "/s/keywords="
            self.searchQuery = "%20".join(self.searchRaw)
        elif self.engine == "twitter":
            self.searchQuery = " ".join(self.searchRaw)
        else:
            self.searchQuery = "+".join(self.searchRaw)
        #end of search exceptions
        self.url = "http://www." + self.engine + "." + self.domain + self.searchString + self.searchQuery

        html = self.url; 
        req = urllib.request.Request(html, headers={'User-Agent': 'Mozilla/5.0'})

        soup = BeautifulSoup(urlopen(req).read(),"html.parser")

        #Regex
        reg=re.compile(".*&sa=")

        links = []

        #Parsing web urls
        for item in soup.find_all('h3', attrs={'class' : 'r'}):
    
            line = (reg.match(item.a['href'][7:]).group())
            links.append(line[:-4])

        #printing links scrapped as a list
        print(links)

        return self.url 
    # end of webspider

   # def openBrowser(self):
    #    webbrowser.open_new_tab(self.url)
    #end of openBrowser()
    
    def handleArgs(self, args):
        if args.engine is not None:
            self.setEngine(args.engine[0])

        if args.domain is not None:
            self.setDomain(args.domain[0])

        for search in args.s:
            self.setQuery(search)
            self.buildLink()
         #   self.openBrowser()
    #end of handleArgs
 
#end of Query