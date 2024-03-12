import requests
from bs4 import BeautifulSoup
import time
import random
import datetime

job_type_array = [ "remote", "data-analytics", "design-ux", "dev-engineering", "operations", "product", "project-management" ]
key_words = ["aws", "amazon web services", "azure", "ai", "ml", "python", "c#", "java", "javascript", ".net", "dotnet", "cloud services", "react", "angular", 
            "docker", "c++", "api", "kafka", "jupyter", "mysql", "nosql", "testing", "mongodb", "node.js", "oracle", "postgresql", "spring", "salesforce"
            "typescript", "kubernetes", "figma", "django", "vue.js", "html", "ruby", "css", "flask", "swift", "sql server", "google cloud platform", "jenkins",
            "git", "github", "saas", "gitlab", "agile", "scrum", "kanban", "devops", "restful api", "graphql", "spring boot", "spring framework", "hibernate",
            "apache kafka", "rabbitmq", "elasticsearch", "memcached", "tensorflow", "pytorch", "redis", "tensorflow", "pytorch", "keras", "machine learning",
            "artificial intelligence", "computer vision", "big data", "firebase", "spark", "cassandra", "hbase", "couchbase", "express.js", "socket.io", "redux", 
            "infrastructure", "websockets", "oauth", "json web token", "JWT", "lambda function", "jira", "serverless architecture", "selenium", "confluence", 
            "trello", "slack", "zoom", "microsoft teams", "skype", "intellij", "vs code", "visual studio code", "pycharm", "eclipse", "sublime text", "atom",
            "vim", "bash", "powershell", "linux", "unix", "xamarin", "microsoft office suite", "m365" ]

# this method does a get on the built in chicago site to determine
# the number of pages to loop through for scraping.
def findNumPages():
    number_of_pages_array = []
    for job_type in range(0, len(job_type_array)):
        print("job_type: ", job_type_array[job_type])
        URL = f"https://www.builtinchicago.org/jobs/{job_type_array[job_type]}"
        print(URL)

        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")

        results = soup.find(id="pagination")

        pagination_navigation_buttons = results.find_all("a", class_="page-link border rounded fw-bold border-0")

        for pagination_navigation_button in pagination_navigation_buttons:
            number_of_pages = int(pagination_navigation_button.string.strip())
            number_of_pages_array.append(number_of_pages)
            # number_of_pages = max(number_of_pages, int(pagination_navigation_button.string.strip()))

    print("Number of Pages:", number_of_pages_array)
    return number_of_pages_array

num_pages_array = findNumPages()
scraping_data_results = {
    "job_id" : [],
    "job_type": job_type_array,
    "job_title": [],
    "company_name" : [],
    "job_link" : [],
    "company_link": [],
    "first_seen": [],
    "last_seen": [],
    "days_active": [],
    "raw_html": [],
    "relevancy_score": [],
    "key_words_found": [],
    "is_active": [],
}

# print(scraping_data_results)

def getPageX():
    for job_type in range(0, len(job_type_array)):
        for num_page in range(1, 2): # replace 2 with job_type + 1
            time_delay = random.randrange(random.randrange(15,17), random.randrange(30,40))
            print("Outer time delay:", time_delay)
            time.sleep(time_delay)

            URL = f"https://www.builtinchicago.org/jobs/{job_type_array[job_type]}"
            page = requests.get(URL)

            soup = BeautifulSoup(page.content, "html.parser")

            results = soup.find(id="jobs-list")
            scraping_data_results["raw_html"].append(results)

            # search results top & bottom jobs section:
            job_elements = results.find_all("div", class_="position-relative job-bounded-responsive border rounded-3 border-gray-02 position-relative bg-white p-md")

            for job_element in job_elements:
                time_delay = random.randrange(random.randrange(15,17), random.randrange(30,40))
                print("Inner time delay:", time_delay)
                time.sleep(time_delay)

                job_title_element = job_element.find("a", id="job-card-alias")
                company_name_element = job_element.find("span")
                job_link = job_element.find("a", id="job-card-alias")["href"]
                apply_url = "https://www.builtinchicago.org" + job_link
                employer_link = job_element.find("a", class_="mb-sm d-inline-flex align-items-center text-pretty-blue link-visited-color z-1")["href"]
                company_url = "https://www.builtinchicago.org" + employer_link
                job_id_element = apply_url[-6:]
            
                scraping_data_results["job_title"] = job_title_element
                scraping_data_results["company_name"] = company_name_element
                scraping_data_results["job_link"] = apply_url
                scraping_data_results["company_link"] = company_url
                scraping_data_results["job_id"] = job_id_element
                scraping_data_results["is_active"] = True
                print(job_title_element.text)
                print(company_name_element.text)
                print(apply_url)
                print(company_url)
                print(job_id_element)
                print()

                for job_id in scraping_data_results["job_id"]:
                    if job_id.find(job_id_element) != -1:
                        # job_id already exists
                        scraping_data_results["last_seen"] = datetime.now()
                    else:
                        # job_id DNE
                        scraping_data_results["first_seen"] = datetime.now()



            # elite results jobs section:
            job_elements = results.find_all("div", class_="featured-jobs border rounded-3 border-gray-02 p-md position-relative bg-white")

            for job_element in job_elements:
                time_delay = random.randrange(random.randrange(15,17), random.randrange(30,40))
                print("Inner time delay:", time_delay)
                time.sleep(time_delay)

                job_title_element = job_element.find("a", class_="mb-0")
                company_name_element = job_element.find("span", class_="fw-medium text-pretty-blue")
                job_link = job_element.find("a", class_="mb-0")["href"]
                apply_url = "https://www.builtinchicago.org" + job_link
                employer_link = job_element.find("a", class_="mb-sm d-inline-flex align-items-center link-visited-color")["href"]
                company_url = "https://www.builtinchicago.org" + employer_link
                job_id_element = apply_url[-6:]

                scraping_data_results["job_title"] = job_title_element
                scraping_data_results["company_name"] = company_name_element
                scraping_data_results["job_link"] = apply_url
                scraping_data_results["company_link"] = company_url
                scraping_data_results["job_id"] = job_id_element
                scraping_data_results["is_active"] = True
                print(job_title_element.text)
                print(company_name_element.text)
                print(apply_url)
                print(company_url)
                print(job_id_element)
                print()

                for job_id in scraping_data_results["job_id"]:
                    if job_id.find(job_id_element) != -1:
                        # job_id already exists
                        scraping_data_results["last_seen"] = datetime.now()
                    else:
                        # job_id DNE
                        scraping_data_results["first_seen"] = datetime.now()


getPageX()

def analysis_of_html_for_relevancy():
    for job_html in scraping_data_results["raw_html"]:
        words_to_add = []
        for job_html_element in job_html:
            for key_word in key_words:
                if job_html_element.find(key_word) != -1:
                    # word is in html
                    scraping_data_results["key_words_found"] = words_to_add.append(key_word)
    
        # calculate and store relevancy: found key words /  total key words
        relevancy_score = len(words_to_add) / len(key_words)
        scraping_data_results["relevancy_score"] = relevancy_score
        


# TODO:
#       grab job tech stack
#       save those job info into the 3D array
#       edit for loop to include all pages
#       save data to long-term storage (Azure Cosmos)
#       retrieve in spreadsheet

#       Capture job type, job title, job id (from site), first seen, last seen, days active, company name, text
#       (HTML), job link, company link, relevancy score, tech (words relevant to SPR)

##################################################
# Below is the code to get the bulleted lists inside a specific job-card
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
