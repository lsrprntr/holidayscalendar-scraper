# holidayscalendar-scraper

This aims to scrape the below site(s) for the international holiday dates and name to output it into an .ics file.

https://www.holidayscalendar.com/categories/international/ (outputs export*.ics file)<br>
https://www.timeanddate.com/holidays/fun/ (outputs funexport*.ics file)<br>
where * is the year.

## Requirements
- Python3
- BeautifulSoup4
- ics


## How to use
1. Run holi.py via python.
2. When prompted enter a valid year to be parsed.
3. export*.ics and funexport*.ics files should be exported in the folder where * is the year input.

Otherwise, the current .ics files can be imported. (export2023.ics,funexport2023.ics)


### Psuedoflowchart below:

1. Ask for year input.
2. Connect to site.
3. Parses the table using BeautifulSoup4.
4. Convert data into formats for ics module.
5. Output an export*.ics file where * is the year inputted.


## Troubleshooting/Issues
- 2020 year has an inconsistency in their html source for parsing which returns a type error
- TBA




