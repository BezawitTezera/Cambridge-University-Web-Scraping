**Cambridge University Computer Laboratory Teaching Page Scraper**
This Python script scrapes course information from the Cambridge University Computer Laboratory Teaching page, organizing it into different file formats within specific directories based on the parts mentioned on the webpage.

**Features**
Web Scraping: Extracts course information from the Computer Laboratory Teaching page.
File Organization: Saves course details into .ccf and .dlc files within directories categorized by course parts.
Continuous Scraping: Runs indefinitely with a 10-minute interval to keep data up-to-date.

**Requirements**
Python 3.x
requests
BeautifulSoup

**Usage**
Run the script:
bash
Copy code
python main.py
The script will continuously scrape the Computer Laboratory Teaching page and organize course information into .ccf and .dlc files within directories based on the course parts mentioned on the webpage.

**File Structure**
The scraped data will be organized in the following structure:
mathematica
Copy code
CambridgeCourses/
└── Part/
    ├── Part-1/
    │   ├── Course-1.ccf
    │   ├── Course-2.ccf
    │   └── Part-1.dlc
    ├── Part-2/
    │   ├── Course-1.ccf
    │   └── Part-2.dlc
    └── ...
**
Customization**
Modify the URL in main.py to scrape data from different web pages if needed.
Adjust the time interval in the code (time_wait) to change the scraping frequency.
