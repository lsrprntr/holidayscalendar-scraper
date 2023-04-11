import urllib.request, urllib.parse, urllib.error
import collections
collections.Callable = collections.abc.Callable
from bs4 import BeautifulSoup
from datetime import datetime
from ics import Calendar, Event

#input string
#fyear = str(input("What year?: ____"))
#link = "https://www.holidayscalendar.com/categories/international-"+fyear+"/"

#page request html vomit
page = urllib.request.urlopen('https://www.holidayscalendar.com/categories/international-2023/')
#print(page.read())


soup = BeautifulSoup(page,'html.parser')

#print(soup)

#find table
#tabel = soup.find('table')
#print(tabel)

dates = list()
descriptions = list()

for i in soup.find_all("tr"):
    for k in i.find_all("td"):
        strng = str(k.text).split()
        if strng is None:
            continue
        strng = " ".join(strng)
        dates.append(strng)

print(dates)



c = Calendar()
e = Event()
e.name = "My cool event"
e.begin = '2014-01-01 00:00:00'
c.events.add(e)
c.events

with open('my.ics', 'w') as f:
    f.writelines(c.serialize_iter())
    f.writelines(c.serialize_iter())