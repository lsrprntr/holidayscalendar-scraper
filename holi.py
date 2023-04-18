import urllib.request, urllib.parse, urllib.error
import collections
collections.Callable = collections.abc.Callable #fixes bs4 exception
from bs4 import BeautifulSoup
import datetime
from ics import Calendar, Event

#year string input with default to 2023 if no input
fyear = str(input("What year?: ")) 
if fyear:
    link = "https://www.holidayscalendar.com/categories/international-"+fyear+"/"
else:
    link = 'https://www.holidayscalendar.com/categories/international-2023/'

#html page reuest and read
try:
    page = urllib.request.urlopen(link)
    #print(page.read())
except:
    fhand = open("demo.html","r")
    page = fhand.read()

#soup handle, the ladle
soup = BeautifulSoup(page,'html.parser')


dates = list()
descriptions = list()

#finding the table and appending to list
for i in soup.find_all("tr"):
    for d in i.find_all("td",class_="wphc-tbl-date"):
        date = (d.text).split() #date list MMM/DD/DAY
        dates.append(date)
    for n in i.find_all("td",class_="wphc-tbl-name d-flex"):
        category = n.find("a").text
        #country = n.find_all("span") #for categories and countries
        descriptions.append(category)

#zip iterator for days and descriptions; also converting days into ISO format for ics module
for a,b in zip(dates,descriptions):
    for x in a:
        continue

        


#ics append
"""
c = Calendar()
e = Event()
e.name = "My cool event"
e.begin = '2014-01-01 00:00:00'
c.events.add(e)
c.events

with open('my.ics', 'w') as f:
    f.writelines(c.serialize_iter())
    f.writelines(c.serialize_iter())

"""