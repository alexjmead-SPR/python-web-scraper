import requests
from bs4 import BeautifulSoup

# url of the website 
base_URL = "https://pythonjobs.github.io"
page = requests.get(base_URL)

# print(page.text)

# parses the html from the requests GET
soup = BeautifulSoup(page.content, "html.parser")

# filters and only saves the html that is within the tag with a class called "job_list"
results = soup.find(class_="job_list")
# print(results.prettify())

# print('\n''\n''\n''\n''\n')

# filters and only saves the html that is within a div tag with a class called "job"
job_elements = results.find_all("div", class_="job")

# # loop that shows everything in the job_elements object
# for job_element in job_elements:
#     print(job_element, end="\n"*2)

# loop that loops through only the job_elements object. This for loop is looking for specific html tags with specific sub-tags or classes. 
# the element is strips to only show the text. These are the results we care about and this text is what is printed.
for job_element in job_elements:

    title_element = job_element.find("h1").find("a").get_text(strip=True)
    company_element = job_element.select_one("span.info > i.i-company").find_next_sibling(string=True).strip()
    date_element = job_element.select_one("span.info > i.i-calendar").find_next_sibling(string=True).strip()
    location_element = job_element.select_one("span.info > i.i-globe").find_next_sibling(string=True).strip()
    read_more_link = job_element.find("a", class_="go_button")["href"]

    #######################
    # below continues the scraping by drilling into the 'read more' button on each job listing. 
    # the read more page has more information that we care about and want to print
    #######################

    # process is repeated from beginning to scrape new url

    # new link of the read more button
    full_url = base_URL  + read_more_link

    # get request to receive the html
    read_more_page = requests.get(full_url)

    # parese the read more page's reqeusts GET
    read_more_soup = BeautifulSoup(read_more_page.content, "html.parser")

    read_more_results = read_more_soup.find(class_="job")
    # print(read_more_results.prettify())

    read_more_contact_elements = read_more_results.find_all("div", class_="contact")

    contact_names = read_more_results.find_all(
        "div", string=lambda text: " Name: " in text.lower()
    )

    contact_names_elements = [
        div_element.parent.parent.parent for div_element in contact_names
    ]

    for contact_name_element in read_more_contact_elements:
        print(contact_name_element)
        contact_name = contact_name_element.find("div", class_="field")

    # for read_more_contact_element in read_more_contact_elements:
    #     print(read_more_contact_element)
    #     asdf = read_more_contact_element.find("div", string=" Name: ").get_text(strip=True)
    #     contact_name = read_more_contact_element.find("div").find("span").get_text(strip=True)
    #     # contact_email = read_more_contact_element.find("div", string="Email:").find("span").get_text(strip=True)
    #     # contact_email = read_more_contact_element.find("div").find("span").find("a").get_text(strip=True)
    #     # contact_website = read_more_contact_element.select_one("div.info > span").find_next_sibling(string=True).strip()

    print("************************")
    # print(contact_name.text.strip())
    # print(contact_email)
    # print(contact_website)
    print("************************")


    # print()
    # print("Job title: " + title_element)
    # print("Company: " + company_element)
    # print("Start date: " + date_element)
    # print("Location: " + location_element)
    # print()
