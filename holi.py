import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

fyear = str(input("What year?: ____"))
link = "https://www.holidayscalendar.com/categories/international-"+fyear+"/"

#page request html vomit
page = urllib.request.urlopen('https://www.holidayscalendar.com/categories/international-2023/')
#print(page.read())


soup = BeautifulSoup(page, 'html.parser')

#print(soup)

#find table
#tabel = soup.find('table')
#print(tabel)


for i in soup.find_all("tr"):
    for k in i.find_all("td"):
        #print(k.text)
        strng = str(k.text).split()
        print("This is the string:",strng)
