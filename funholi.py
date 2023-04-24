import urllib.request, urllib.parse, urllib.error
import collections
collections.Callable = collections.abc.Callable #fixes bs4 exception
from bs4 import BeautifulSoup
import datetime
from ics import Calendar, Event
import os

#File name format;
fyear = "2023"
filename = f'funexport{fyear}.ics'

##Fun holidays export and parse from timeanddate site
#html page request and read; exception to local file
try:
    link = "https://www.timeanddate.com/holidays/fun/"
    page = urllib.request.urlopen(link)
except:
    fhand = open("fundemo.html","r")
    page = fhand.read()
#soup handle, the ladle
soup = BeautifulSoup(page,'html.parser')

dates = list()
descriptions = list()

#table parsing and converting to iso format
for x in soup.find_all("tr"):
    if len(x)==3:
        date = x.contents[0].text #%d %mmm        
        if date[0].isnumeric():
            description = x.contents[2].text #holiday name
            date_time_str = fyear+" "+date #initial string setup before function translation
            date_time_obj = datetime.datetime.strptime(date_time_str, '%Y %d %b')
            dates.append(date_time_obj)
            descriptions.append(description)

    
#check if file created if so delete
if os.path.isfile(filename):
    os.remove(filename)
    print("Deleting old funexport.ics file")

#create file export;

with open(filename, 'w') as f:
    c = Calendar() #create calendar object
    
    #zip ip iterator for days and descriptions;
    for a,b in zip(dates,descriptions):
        e = Event()
        
        #if len(b)>66: #for SUMMARY: description standards might error for 75 characters
        #    b=b[:66]+b[66:] #75 character warning format to be edited if needed

        #building event details
        e.name = b
        e.begin = a
        e.make_all_day()
        e.transparent = "Transparent"
        
        #add event to calendar object
        c.events.add(e)

    #writes calendar to file
    f.writelines(c.serialize_iter())
    
print("funexport.ics created")