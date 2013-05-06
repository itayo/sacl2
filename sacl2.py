import urllib2
from urlparse import urlparse, urlunparse
from HTMLParser import HTMLParser
from time import gmtime,strftime,localtime
import xml.etree.ElementTree as ET
import xlwt
from datetime import datetime
debug = True
_ENTERING=1
_EXITING=0
def logger(func,status):
    if debug:
        if status == _ENTERING:
            print "Entering",func
        if status == _EXITING:
            print "Exiting", func
        
        
    
def isDebug():
     return debug
def parseXML(url='https://steamcommunity.com/profiles/76561198035378506/stats/CivV?l=english&xml=1',test=False,proxy=None):
    logger(parseXML,_ENTERING)
    done = []
    todo = []
    print "data reding"
    if proxy==None and test == False:
        data = urllib2.urlopen(url).read()
    elif proxy != None and test == False:
       proxy = urllib2.ProxyHandler()
       ul2 = urllib2.build_opener(proxy)
       data= ul2.open(url).read()
    else:
        f= open("testdata/test.html","r")
        data = f.read()
        f.close()      
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
    logger(parseXML,_EXITING)
    return done,todo
                
def genExcel(done,todo):
    font0 = xlwt.Font()
    font0.name = 'Times New Roman'
    font0.colour_index = 2
    font0.bold = True
    style0 = xlwt.XFStyle()
    style0.font = font0
    wb = xlwt.Workbook()
    wsTodo= wb.add_sheet("Achievements Todo")
    wsDone= wb.add_sheet("Achievements done")
    
    todoRow=doneRow=1
    
    wsDone.write(0,0,'Name')
    wsDone.write(0,1,'Date')
    wsDone.write(0,2,'Desc')
    for x in done:
        wsDone.write(doneRow,0,x['name'])
        wsDone.write(doneRow,1,x['readableDate'])
        wsDone.write(doneRow,2,x['desc'])
        doneRow +=1
    wsTodo.write(0,0,'Name')
    wsTodo.write(0,1,'Desc')        
    for x in todo:
        wsTodo.write(todoRow,0,x['name'])
        wsTodo.write(todoRow,1,x['desc'])        
        todoRow +=1
    wb.save("test.xls")
    
    
def main():
    if False:
        url=raw_input("Enter full link to achievement page:")    
        (done,todo)=parseXML(url)
    
    print "start"    
    (done,todo)=parseXML()
    genExcel(done,todo)
    




if __name__ == "__main__":
    main()

