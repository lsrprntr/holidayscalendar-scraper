# holidayscalendar-scraper

This aims to scrape the below site(s) for the international holiday dates and name to output it into an .ics file.<br>
https://www.holidayscalendar.com/categories/international/<br>
https://www.timeanddate.com/holidays/fun/<br>
<br>
<br>
### Psuedoflowchart below:<br>
1. Ask for year input.<br>
2. Connect to site.<br>
3. Parses the table using BeautifulSoup4.<br>
4. Convert data into formats for ics module.<br>
5. Output an export*.ics file where * is the year inputted.

## Requirements
Requires Python3,BeautifulSoup4, and ics library.


## How to use


1. Run holi.py via python.
2. When prompted enter a valid year to be parsed.
3. .ics file should be exported in the folder.

## Troubleshooting
TBA


Year 2020 has an inconsistency in their html source for parsing which returns a type error




