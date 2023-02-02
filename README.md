# UCSBHistoricalCourseScraper

Finds all courses and their respective names for certain class subjects using their shortened classification (e.g. ECE, CMPSC for Electrical Engineering and Computer Science) and compiles each quarter of the last year into a quarter-specific csv file for use in Excel or Google Sheets. This is accomplished through website scraping of the UCSB course website, this speeds up the process for searching through every course significantly. Some setbacks were the loading speed of the UCSB website itself, so I had to slow down the script at certain places so that the data could be read.

## Getting Started

These instructions will give you a copy of the project up and running on
your local machine for development and testing purposes. See deployment
for notes on deploying the project on a live system.

### Prerequisites

Requirements for the software and other tools to build, test, and push
- [Chrome Driver](https://chromedriver.chromium.org/getting-started)
- [Selenium and Pandas Python Packages](https://packaging.python.org/en/latest/tutorials/installing-packages/)
 
 The chrome driver is needed in addition to an installation of python to run the script.
 Hopefully, this program is useful and makes it easier to choose classes!
