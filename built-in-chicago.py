import requests
from bs4 import BeautifulSoup
from pprint import pprint

URL = "https://www.builtinchicago.org/jobs"
page = requests.get(URL)

# print(page.text)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="jobs-list")
# print(results.prettify())

job_elements = results.find_all("div", id="job-card-3532708")

for job_element in job_elements:
    title_element = job_element.find("a", id="job-card-alias")
    company_element = job_element.find("span")
    print(title_element.text)
    print(company_element.text)
    print()

    link = job_element.find_all("a")[1]["href"]
    apply_url = "https://www.builtinchicago.org" + link
    print(f"Apply here: {apply_url}\n")

    page = requests.get(apply_url)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(class_="job-description")

    job_description_elements = results.find_all("ul")
    job_description_length = len(job_description_elements)
    # print(job_description_length)

    for i in range(0,job_description_length):
      for job_description_element in job_description_elements[i]:
        print(job_description_element.text)
      print()
