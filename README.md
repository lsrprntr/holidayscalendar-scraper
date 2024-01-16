# holidayscalendar-scraper

This aims to scrape the below site(s) for the international holiday and fun holidays to output it into an .ics file.

https://www.holidayscalendar.com/categories/international/ (outputs export*.ics file)<br>
https://www.timeanddate.com/holidays/fun/ (outputs funexport*.ics file)<br>
where * is the year.

## Requirements
- Python3 [Link to install](https://wiki.python.org/moin/BeginnersGuide/Download)
- BeautifulSoup4 [Link to install](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)
- ics [Link to install](https://icspy.readthedocs.io/en/stable/)


## How to use
1. Install above requirements
2. Run holi.py via python.
3. When prompted enter a valid year to be parsed.
4. export*.ics and funexport*.ics files should be exported in the folder where * is the year input.

Otherwise, the current .ics files can be downloaded and imported. (export*.ics,funexport*.ics) where * is the year.

![image](https://github.com/lsrprntr/holidayscalendar-scraper/assets/39038103/6c5d4b0d-f42c-4b17-b64a-de6c3a45674c)


### Psuedoflowchart below:

```mermaid
graph TD;
    A[Ask for year input] --> B(Connect to website);
    B-->C(Parses website with BeautifulSoup);
    C-->D(Convert data into formats for ics module);
    D-->E(Output an export*.ics file where * is the year inputted);
```

## Troubleshooting/Issues
- ~~Not working for Windows devices.~~ fixed
- ~~2020 year has an inconsistency in their html source for parsing which returns a type error.~~ fixed
- ~~Default value will error when new year rolls over until I fix the demo.html~~ fixed



