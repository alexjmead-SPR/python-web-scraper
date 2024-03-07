import requests
from bs4 import BeautifulSoup
from pprint import pprint

# this method does a get on the built in chicago site to determine
# the number of pages to loop through for scraping.
def findNumPages():
    URL = "https://www.builtinchicago.org/jobs"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    results = soup.find(id="pagination")
    print(results.prettify())

    pagination_navigation_buttons = results.find_all("a", class_="page-link border rounded fw-bold border-0")

    for pagination_navigation_button in pagination_navigation_buttons[len(pagination_navigation_buttons) - 1]:
        number_of_pages = pagination_navigation_button.text

    print("Number of Pages: ", number_of_pages)

num_pages = findNumPages()
num_jobs = 20 # staticly determined by website
data = [[]*num_jobs] * num_pages 
# [[job1, job2,...job20], [job1, job2,...job20], [job1, job2,...job20],...,[job1, job2,...job20]] ## 20 jobs per page, ~38 pages

# TODO: 
#       loop through each page and collect the names of the job cards
#       save those job card names (job-card-123456) into the 2D array
#       this array we will want to loop through when all pages have been collected to parse each job for data

#       Capture job name, job title, apply link to share with Sales

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