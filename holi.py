import urllib.request, urllib.parse, urllib.error
import collections
collections.Callable = collections.abc.Callable #fixes bs4 exception
from bs4 import BeautifulSoup
import datetime
from ics import Calendar, Event
import os

#year string input with default to 2023 if no input
today = datetime.date.today()
year = str(today.year)
try:
    fyear = str(input("What year?: "))
except:
    print("Error input: Defaulting to 2023")
    fyear = year
if fyear:
    link = "https://www.holidayscalendar.com/categories/international-"+fyear+"/"
else:
    fyear = year
    link = 'https://www.holidayscalendar.com/categories/international-2023/'

#html page request and read; exception to local file
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

#File name format;
filename = f'export{fyear}.ics'

#check if file created if so delete
if os.path.isfile(filename):
    os.remove(filename)
    print("Deleting old file")

#create file export;
with open(filename, 'w') as f:
    c = Calendar() #create calendar object

    #zip ip iterator for days and descriptions; also converting days into ISO format for ics module
    for a,b in zip(dates,descriptions):
        e = Event()
        date_time_str = fyear+" "+" ".join(a) #initial string setup before function translation
        date_time_obj = datetime.datetime.strptime(date_time_str, '%Y %b %d %A')

        if len(b)>66: #for SUMMARY: description standards might error for 75 characters
            b=b[:66]+b[66:] #75 character warning format to be edited if needed

        #building event details
        e.name = b
        e.begin = date_time_obj
        e.end = date_time_obj
        e.transparent = "Transparent"
        e.categories = "Holidays"
        e.make_all_day
        
        #add event to calendar object
        c.events.add(e)

    #writes calendar to file
    f.writelines(c.serialize_iter())
        

print(f"{filename} created")
