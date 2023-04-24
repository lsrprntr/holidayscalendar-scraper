# holidayscalendar-scrapper

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
5. Output an export*.ics file where * is the year inputted.<br>
<br>
## Requirements
Requires Python3,BeautifulSoup4, and ics library.<br>
<br>

## How to use
1. Run holi.py via python.<br>
2. When prompted enter a valid year to be parsed.<br>
3. .ics file should be exported in the folder.<br>

## Troubleshooting
TBA
<br>



