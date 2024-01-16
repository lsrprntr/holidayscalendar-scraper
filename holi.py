import urllib.request, urllib.parse, urllib.error
import collections
collections.Callable = collections.abc.Callable #fixes bs4 exception
from bs4 import BeautifulSoup
import datetime
from ics import Calendar, Event
import os

'''
// This script parses a list of holidays online and outputs a calendar file in the same folder.
'''

# Gets current year as default string input if no input given
today = datetime.date.today()
year = str(today.year)

# Gets user input
try:
    fyear = str(int(input("What year?: ")))
    print(f"Parsing for {fyear} year")
except:
    fyear = year
    print(f"Error year input: Defaulting to {fyear}")

if 999<int(fyear)<10000: #if blank use default year
    link = "https://www.holidayscalendar.com/categories/international-"+fyear+"/"
else:
    fyear = year
    link = "https://www.holidayscalendar.com/categories/international-"+fyear+"/"
    print(f"Error blank input: Defaulting to {fyear}")

# HTML page request and read; exception to local file
try:
    page = urllib.request.urlopen(link)
except:
    fhand = open("intdemo.html","r")
    page = fhand.read()

# soup handle, the ladle
soup = BeautifulSoup(page,'html.parser')

dates = list()
descriptions = list()

# finding the table and appending to list
for i in soup.find_all("tr"):
    for d in i.find_all("td",class_="wphc-tbl-date"):
        date = (d.text).split() #date list MMM/DD/DAY
        dates.append(date)
    for n in i.find_all("td",class_="wphc-tbl-name d-flex"):
        name = n.find("a").contents[0] #day description
        #country = n.find_all("span") #for categories and countries
        descriptions.append(name)
        
# File name format;
filename = f'export{fyear}.ics'

# Check if file created if so delete
if os.path.isfile(filename):
    os.remove(filename)
    print(f"Deleting old {filename} file")

# Create file export;
with open(filename, 'w') as f:
    c = Calendar() #create calendar object

    # zip ip iterator for days and descriptions; also converting days into ISO format for ics module
    for a,b in zip(dates,descriptions):
        e = Event()
        date_time_str = fyear+" "+" ".join(a) #initial string setup before function translation
        try: 
            date_time_obj = datetime.datetime.strptime(date_time_str, '%Y %A, %b %d')
        except:
            print(date_time_str, b, "skipped due to exception")
            continue

        #if len(b)>66: # For SUMMARY: description standards might error for 75 characters
        #    b=b[:66]+b[66:] #75 character warning format to be edited if needed

        # Building event details
        e.name = b
        e.begin = date_time_obj
        e.make_all_day()
        e.transparent = "Transparent"
        
        # Add event to calendar object
        c.events.add(e)

    # Writes calendar to file
    f.writelines(c.serialize_iter())
        
print(f"{filename} created")




'''
https://www.timeanddate.com/holidays/fun/
The site does not have seperate pages for other years and only has one page for the current year.
'''


##Fun holidays export and parse from timeanddate site
#File name format;
filename = f'funexport{fyear}.ics'

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
    print(f"Deleting old {filename} file")

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
    
print(f"{filename} created")
