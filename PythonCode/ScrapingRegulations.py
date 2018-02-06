import requests, bs4, sqlite3, re, time, os
from datetime import timedelta

RootDir = os.getcwd()
print RootDir

def checkDir(chap,pt):
    os.chdir(RootDir)
    directory = 'Chapter'+str(chap)
    print directory
    if not os.path.isdir(directory):
        os.mkdir(directory)
        os.chdir(directory)
        ActualScraper(chap,pt)
        os.chdir(RootDir)
    else:
        os.chdir(directory)
        ActualScraper(chap,pt)
        os.chdir(RootDir)

def ActualScraper(chapter,part):
   # os.chdir(RootDir)
    print 'Scraper in action for '+str(chapter)+' '+str(part)
    WebAddress = "https://www.ecfr.gov/cgi-bin/text-idx?SID=de612e6019996ddb79809a334a4da89b&mc=true&node=pt12."+str(chapter)+"."+str(part)+"&rgn=div5"
    myPage = requests.get(WebAddress)
    mysoup = bs4.BeautifulSoup(myPage.content,"lxml")
   # directory = 'Chapter '+str(chapter)
  #  print directory
  #  if not os.path.isdir(directory):
  #      print 'meow'
  #      os.mkdir(directory)
  #      os.chdir(directory)
  #      print os.getcwd()
  #      
    myFile = open('Scraped_'+str(chapter)+'_'+str(eachNum)+'.txt','w')
    ParaList = mysoup.findAll('p')
    for eachP in ParaList:
        try:
            ParaText = eachP.text
            myFile.write(ParaText+'\n')
        except:
            pass
    myFile.close()

start_time = time.time()
myRange = range(1,1900)
for eachNum in myRange:
    if 1 <= eachNum <= 195:
        print 'Now on Chapter 1 Section '+str(eachNum)
        #ActualScraper(1,eachNum)
        checkDir(1,eachNum)
    elif 200 <= eachNum <= 219:
        print 'Now on Chapter 2_1 Section '+str(eachNum)
        checkDir(2,eachNum)
    elif 220 <= eachNum <= 229:
        print 'Now on Chapter 2_2 Section '+str(eachNum)
        checkDir(2,eachNum)
    elif 230 <= eachNum <= 299:
        print 'Now on Chapter 2_3 Section '+str(eachNum)
        checkDir(2,eachNum)
    elif 300 <= eachNum <= 399:
        print 'Now on Chapter 3 Section '+str(eachNum)
        checkDir(3,eachNum)
    elif 400 <= eachNum <= 499:
        print 'Now on Chapter 4 Section '+str(eachNum)
        checkDir(4,eachNum)
    elif 500 <= eachNum <= 599:
        print 'Now on Chapter 5 Section '+str(eachNum)
        checkDir(5,eachNum)
    elif 600 <= eachNum <= 699:
        print 'Now on Chapter 6 Section '+str(eachNum)
        checkDir(6,eachNum)
    elif 700 <= eachNum <= 799:
        print 'Now on Chapter 7 Section '+str(eachNum)
        checkDir(7,eachNum)
    elif 800 <= eachNum <= 899:
        print 'Now on Chapter 8 Section '+str(eachNum)
        checkDir(8,eachNum)
    elif 900 <= eachNum <= 999:
        print 'Now on Chapter 9 Section '+str(eachNum)
        checkDir(9,eachNum)
    elif 1000 <= eachNum <= 1025:
        print 'Now on Chapter 10 Section '+str(eachNum)
        checkDir(10,eachNum)
    elif 1026 <= eachNum <= 1099:
        print 'Now on Chapter 10 Section '+str(eachNum)
        checkDir(10,eachNum)
    elif 1100 <= eachNum <= 1199:
        print 'Now on Chapter 11 Section '+str(eachNum)
        checkDir(11,eachNum)
    elif 1200 <= eachNum <= 1299:
        print 'Now on Chapter 12 Section '+str(eachNum)
        checkDir(12,eachNum)
    elif 1300 <= eachNum <= 1399:
        print 'Now on Chapter 13 Section '+str(eachNum)
        checkDir(13,eachNum)
    elif 1400 <= eachNum <= 1499:
        print 'Now on Chapter 14 Section '+str(eachNum)
        checkDir(14,eachNum)
    elif 1500 <= eachNum <= 1599:
        print 'Now on Chapter 15 Section '+str(eachNum)
        checkDir(15,eachNum)
    elif 1600 <= eachNum <= 1699:
        print 'Now on Chapter 16 Section '+str(eachNum)
        checkDir(16,eachNum)
    elif 1700 <= eachNum <= 1799:
        print 'Now on Chapter 17 Section '+str(eachNum)
        checkDir(17,eachNum)
    elif 1800 <= eachNum <= 1899:
        print 'Now on Chapter 18 Section '+str(eachNum)
        checkDir(18,eachNum)

#removing empty files
for root,dirs,files in os.walk(RootDir):
    for f in files:
        name = os.path.join(root,f)
        try:
            if os.path.getsize(name) <= 200:
                print name
                os.remove(name)
        except WindowsError:
            continue

print 'Complete'
print "My program took", time.time() - start_time, "to run"

      