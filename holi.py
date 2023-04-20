import urllib.request, urllib.parse, urllib.error
import collections
collections.Callable = collections.abc.Callable #fixes bs4 exception
from bs4 import BeautifulSoup
import datetime
from ics import Calendar, Event
import os

#year string input with default to 2023 if no input
fyear = str(input("What year?: "))
if fyear:
    link = "https://www.holidayscalendar.com/categories/international-"+fyear+"/"
else:
    fyear="2023"
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

#check if file created if so delete
if os.path.isfile("export.ics"):
    os.remove("export.ics")
    print("Deleting old file")

#create file export;
with open('export.ics', 'w') as f:
    c = Calendar()
    #zip ip iterator for days and descriptions; also converting days into ISO format for ics module
    for a,b in zip(dates,descriptions):
        
        e = Event()
        date_time_str = fyear+" "+" ".join(a) #initial string setup before function
        date_time_obj = datetime.datetime.strptime(date_time_str, '%Y %b %d %A')

        if len(b)>66:
            b=b[:66]+b[66:] #75 character warning format to be edited if needed

        #building event details
        e.name = b
        e.begin = date_time_obj
        e.end = date_time_obj
        e.make_all_day()
        
        #e.extra = "help"
        #adding to calendar 
        c.events.add(e)

        #breakpoint = input("Input to continue")

        #write to file
        #print(e)
        #f.writelines(e.serialize_iter())
        #f.writelines("\n")
    
    #writes calendar to file
    f.writelines(c.serialize_iter())
        

print("export.ics created")
