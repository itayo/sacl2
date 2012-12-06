import urllib2
from urlparse import urlparse, urlunparse
from HTMLParser import HTMLParser
#from xml.dom.minidom import parseString
#from xml.dom import minidom
from time import gmtime,strftime,localtime
import xml.etree.ElementTree as ET
debug=True

def parseXML(url='https://steamcommunity.com/profiles/76561198035378506/stats/CivV?l=english&xml=1'):
    done = []
    todo = []
    data = urllib2.urlopen(url).read()
    root = ET.fromstring(data)
    for node in root:
        if node.tag == "achievements":
            for ach in node:
                unlockTime=None
                for d in ach:
                    if d.tag == "name":
                        name=d.text
                    if d.tag == "description":
                        desc=d.text
                    if d.tag == "unlockTimestamp":
                        unlockTime=int(d.text)
                p = {}
                p['name']=name
                p['desc']=desc

                if unlockTime == None:
                    todo.append(p)
                else:
                    p['readableDate']=strftime("%b %d, %Y %I:%m %p",localtime(unlockTime))
                    p['unixTime']=unlockTime
                    done.append(p)
                print p
    return done,todo
                

                

    
    
def main():
    if debug == False:
      url=raw_input("Enter full link to achievement page:")    
      (done,todo)=parseXML(url)
    else:
      (done,todo)=parseXML()

    print done
    print todo




if __name__ == "__main__":
    main()

