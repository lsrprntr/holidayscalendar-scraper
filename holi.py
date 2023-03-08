
import urllib.request, urllib.parse, urllib.error


page = urllib.request.urlopen('https://www.holidayscalendar.com/categories/international/')
print(page.read())
