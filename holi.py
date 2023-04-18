import urllib.request, urllib.parse, urllib.error
import collections
collections.Callable = collections.abc.Callable
from bs4 import BeautifulSoup
from datetime import datetime
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
#print(soup)

dates = list()
descriptions = list()

#finding the table
for i in soup.find_all("tr"):
    for k in i.find_all("a"):
        print(k)
        #strng = str(k.text).split()
        #if strng is None:
        #    continue
        #strng = " ".join(strng)
        #dates.append(strng)

print(dates)


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