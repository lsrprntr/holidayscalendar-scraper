
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

page = urllib.request.urlopen('https://www.holidayscalendar.com/categories/international/')
#print(page.read())

soup = BeautifulSoup(page, 'html.parser')

print(soup.prettify())
