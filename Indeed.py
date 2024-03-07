import requests
from bs4 import BeautifulSoup

URL = "https://www.builtinchicago.org/jobs"
page = requests.get(URL)

print(page.text)

soup = BeautifulSoup(page.content, "hmtl.parser")

results = soup.find(id="jobs-list")
print(results.prettify())

job_elements = results.find_all("div", class_="card-content")

