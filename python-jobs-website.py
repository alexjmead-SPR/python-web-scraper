import requests
from bs4 import BeautifulSoup

URL = "https://pythonjobs.github.io/"
page = requests.get(URL)

# print(page.text)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(class_="job_list")
# print(results.prettify())

job_elements = results.find_all("div", class_="job")

# for job_element in job_elements:
#     print(job_element, end="\n"*2)

# python_jobs = results.find_all(
#     "span", string=lambda in text.lower()
# )

# python_job_elements = [
#     h2_element.parent.parent.parent for h2_element in python_jobs
# ]

for job_element in job_elements:
    title_element = job_element.find("h1")
    location_element = job_element.select_one("span.info > i.i-globe").find_next_sibling(string=True).text.strip()
    start_date_element = job_element.select_one("span.info > i.i-calendar").find_next_sibling(string=True).text.strip()
    company_element = job_element.select_one("span.info > i.i-company").find_next_sibling(string=True).text.strip()
    description_element = job_element.find("p", class_="detail")
    print(title_element.text.strip())
    print(location_element)
    print(start_date_element)
    print(company_element)
    print(description_element.text.strip())
    print()

    # details = job_element.find_all("span", class_="info")
    # for detail in details:
    #     detail_location = job_element.find_all("span")[0]
    #     detail_company = job_element.find_all("span")[3]
    #     print(detail_location.text.strip())
    #     print(detail_company.text.strip())

# print(len(python_jobs))
