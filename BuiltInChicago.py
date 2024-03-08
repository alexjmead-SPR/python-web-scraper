import requests
from bs4 import BeautifulSoup
import time
import random

# this method does a get on the built in chicago site to determine
# the number of pages to loop through for scraping.
def findNumPages():
    URL = "https://www.builtinchicago.org/jobs"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(id="pagination")

    pagination_navigation_buttons = results.find_all("a", class_="page-link border rounded fw-bold border-0")

    number_of_pages = 0

    for pagination_navigation_button in pagination_navigation_buttons:
        number_of_pages = max(number_of_pages, int(pagination_navigation_button.string.strip()))

    print("Number of Pages:", number_of_pages)
    return number_of_pages

num_pages = findNumPages()
num_jobs = 20 # staticly determined by website
num_job_details = 4
data = [[[None] * num_job_details for _ in range(num_jobs)] for _ in range(num_pages)]

def getPageX():
    for num_page in range(1, 2): #replace 2 with num_pages + 1
        time_delay = random.randrange(random.randrange(15,17), random.randrange(30,40))
        print("Outer time delay:", time_delay)
        time.sleep(time_delay)

        URL = "https://www.builtinchicago.org/jobs"
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")

        results = soup.find(id="jobs-list")

        job_elements = results.find_all("div", class_="position-relative job-bounded-responsive border rounded-3 border-gray-02 position-relative bg-white p-md")

        for job_element in job_elements:
            time_delay = random.randrange(random.randrange(15,17), random.randrange(30,40))
            print("Inner time delay:", time_delay)
            time.sleep(time_delay)

            job_title_element = job_element.find("a", id="job-card-alias")
            company_name_element = job_element.find("span")
            print(job_title_element.text)
            print(company_name_element.text)
            print()

            job_link = job_element.find("a", id="job-card-alias")["href"]
            apply_url = "https://www.builtinchicago.org" + job_link
            print(apply_url)

            employer_link = job_element.find("a", class_="mb-sm d-inline-flex align-items-center text-pretty-blue link-visited-color z-1")["href"]
            company_url = "https://www.builtinchicago.org" + employer_link
            print(company_url)

        job_elements = results.find_all("div", class_="featured-jobs border rounded-3 border-gray-02 p-md position-relative bg-white")

        for job_element in job_elements:
            time_delay = random.randrange(random.randrange(15,17), random.randrange(30,40))
            print("Inner time delay:", time_delay)
            time.sleep(time_delay)

            job_title_element = job_element.find("a", class_="mb-0")
            company_name_element = job_element.find("span", class_="fw-medium text-pretty-blue")
            print(job_title_element.text)
            print(company_name_element.text)
            print()

            job_link = job_element.find("a", class_="mb-0")["href"]
            apply_url = "https://www.builtinchicago.org" + job_link
            print(apply_url)

            employer_link = job_element.find("a", class_="mb-sm d-inline-flex align-items-center link-visited-color")["href"]
            company_url = "https://www.builtinchicago.org" + employer_link
            print(company_url)
getPageX()

# TODO:
#       save those job info into the 3D array
#       edit for loop to include all pages
#       save data to long-term storage (Azure Cosmos?)

#       Capture job name, job title, apply and company link to share with Sales

##################################################
# Below is the code ""to get the bulleted lists inside a specific job-card
##################################################

# URL = "https://www.builtinchicago.org/jobs"
# page = requests.get(URL)

# # print(page.text)

# soup = BeautifulSoup(page.content, "html.parser")

# results = soup.find(id="jobs-list")
# # print(results.prettify())

# job_elements = results.find_all("div", id="job-card-3206669")

# for job_element in job_elements:
#     title_element = job_element.find("a", id="job-card-alias")
#     company_element = job_element.find("span")
#     print(title_element.text)
#     print(company_element.text)
#     print()

#     link = job_element.find_all("a")[1]["href"]
#     apply_url = "https://www.builtinchicago.org" + link
#     print(f"Apply here: {apply_url}\n")

#     page = requests.get(apply_url)

#     soup = BeautifulSoup(page.content, "html.parser")

#     results = soup.find(class_="job-description")

#     job_description_elements = results.find_all("ul")
#     job_description_length = len(job_description_elements)
#     # print(job_description_length)

#     for i in range(0,job_description_length):
#       for job_description_element in job_description_elements[i]:
#         print(job_description_element.text)
#       print()
