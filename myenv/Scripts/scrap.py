import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="ResultsContainer")
# print('these are ' , results)
# print(results.prettify())
job_elements = results.find_all("div", class_="card-content")

for job_element in job_elements:
    print(job_element, end="\n"*2)

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element)
    print(company_element)
    print(location_element)
    print()

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text)
    print(company_element.text)
    print(location_element.text)
    print()

for job_element in job_elements:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()

#Find Elements by Class Name and Text Content
python_jobs = results.find_all("h2", string="Python")
print(python_jobs)

#Pass a Function to a Beautiful Soup Method
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)
print(len(python_jobs))

##### 


python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)
'''
for job_element in python_jobs:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()'''
#####

for job_element in python_jobs:
    title_element = job_element.find("h2", class_="title")
    company_element = job_element.find("h3", class_="company")
    location_element = job_element.find("p", class_="location")
    
    title = title_element.text.strip() if title_element else "N/A"
    company = company_element.text.strip() if company_element else "N/A"
    location = location_element.text.strip() if location_element else "N/A"
    
    print(title)
    print(company)
    print(location)
    print()

# Extract Attributes From HTML Elements

python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)

python_job_elements = [
    h2_element.parent.parent.parent for h2_element in python_jobs
]

for job_element in python_job_elements:
    # -- snip --
    links = job_element.find_all("a")
    for link in links:
        print(link.text.strip())

for job_element in python_job_elements:
    # -- snip --
    links = job_element.find_all("a")
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")

for job_element in python_job_elements:
    link_url = job_element.find_all("a")[1]["href"]
    print(f"Apply here: {link_url}\n")

