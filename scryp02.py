import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

# URL of the site to scrape
url = "https://realpython.github.io/fake-jobs/"
session = requests.Session()
response = session.get(url)
response.encoding = response.apparent_encoding

if response.status_code == 200:
    html = response.text
    # Save the HTML content to a file
    with open("fake_jobs.html", "w") as f:
        f.write(html)
    print('File created')
    
    # Create an empty DataFrame with the desired columns
    columns = ['Job Title', 'Company Name', 'Location', 'Date', 'Apply Link', 'Full Job Description']
    df = pd.DataFrame(columns=columns)
    
    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find all job postings
    job_elements = soup.find_all('div', class_='card-content')
    
    # List to hold job data
    job_data = []
    
    # Loop through each job posting and extract the relevant information
    for job_element in job_elements:
        job_title = job_element.find('h2', class_='title').text.strip()
        company_name = job_element.find('h3', class_='company').text.strip()
        location = job_element.find('p', class_='location').text.strip()
        date = job_element.find('time')['datetime']
        apply_link = job_element.find('a', string='Apply')['href']
        
        # Follow the apply link to get the full job description
        try:
            apply_response = session.get(apply_link)
            apply_response.raise_for_status()
            apply_soup = BeautifulSoup(apply_response.content, 'html.parser')
            full_job_description = apply_soup.find('div', class_='content').text.strip()
        except requests.exceptions.RequestException as e:
            print(f"Failed to retrieve job description for {job_title}: {e}")
            full_job_description = "N/A"
        
        # Append the data to the list
        job_data.append({
            'Job Title': job_title,
            'Company Name': company_name,
            'Location': location,
            'Date': date,
            'Apply Link': apply_link,
            'Full Job Description': full_job_description
        })
        
        # Rate limiting
        time.sleep(1)  # Sleep for 1 second between requests
    
    # Convert the list to a DataFrame and concatenate with the existing DataFrame
    df = pd.concat([df, pd.DataFrame(job_data)], ignore_index=True)
    
    # Display the first three rows of the DataFrame
    print(df.head(3))
else:
    print('error:', response.status_code)

df.to_csv('fake_jobs.csv', index=False)
print('DataFrame written to fake_jobs.csv')