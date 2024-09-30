# Job Scraper
This repository contains a Python script that scrapes job postings from the Real Python Fake Jobs website and saves the data into a CSV file. The script uses the requests library to fetch the HTML content of the website and BeautifulSoup to parse the HTML and extract job details.

## Features
Fetch HTML Content: Retrieves the HTML content of the job listings page.
Parse HTML: Uses BeautifulSoup to parse the HTML and extract job details such as job title, company name, location, date, apply link, and full job description.
Error Handling: Includes error handling for network requests to ensure the script doesn’t break if a request fails.
Rate Limiting: Implements a delay between requests to avoid overwhelming the server.
Save to CSV: Saves the extracted job data into a CSV file for easy access and analysis.

### Requirements
* pandas
* requests
* beautifulsoup4
