import urllib2
from urlparse import urlparse, urlunparse
from BeautifulSoup import BeautifulSoup
from HTMLParser import HTMLParser
from xml.dom.minidom import parseString
from xml.dom import minidom
debug=False

def parseXML(data):
    ach = None
    for a in data.firstChild.childNodes:
       for data in a.childNodes:
           print data.childNodes
    
def getData(url='https://steamcommunity.com/profiles/76561198035378506/stats/CivV?l=english&xml=1'):
    data=minidom.parseString((urllib2.urlopen(url).read()))
    parseXML(data)

def main():
    if debug == False:
      url=raw_input("Enter full link to achievement page:")    
      data=openPage(url)
    else:
      data=getData()

    print data




if __name__ == "__main__":
    main()

