import time
from typing import List
import pandas as pd    
# Selenium #
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


# Driver #
driver = webdriver.Chrome(executable_path=r'C:\Program Files\ChromeDriver\chromedriver.exe')

# Maximize Window
driver.maximize_window()
driver.switch_to.window(driver.current_window_handle)
driver.implicitly_wait(10)

# Enter to the site
driver.get('https://www.linkedin.com/login')
time.sleep(2)

# Accept cookies
# driver.find_element("xpath", "/html/body/div/main/div[1]/div/section/div/div[2]/button[2]").click()

# Login
with open(r"C:\Users\ftbar\.vscode\Python Bots\LinkedInBot\usercredentials.txt", encoding="utf-8") as file:
    user_credentials = file.readlines()
    user_credentials = [line.rstrip() for line in user_credentials]
    user_name = user_credentials[0]
    password = user_credentials[1]

    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(user_name)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    time.sleep(1)

# Login button
driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()
driver.implicitly_wait(30)

# Jobs page
jobs = driver.find_element(By.XPATH, '//*[@id="ember19"]')
driver.execute_script("arguments[0].click();", jobs)
time.sleep(3)

# Search by user's filters (Change LinkedIn filters and then copy the link)
driver.get("https://www.linkedin.com/jobs/search/?geoId=101279968&keywords=intern&location=Buenos%20Aires%20Province%2C%20Argentina&refresh=true")
time.sleep(1)

# Get links
links = []

# Navigate 5 pages
print('Links being collected...')
try:
    jobs_list = list
    for page in range(2,4):
        print(page-1)
        time.sleep(7)
        jobs_block = driver.find_element(By.CLASS_NAME, 'jobs-search-results-list')
        jobs_list.append(jobs_block.find_elements(By.CLASS_NAME, 'job-card-container relative job-card-list'))
        print(jobs_list)
        for job in jobs_list:
            all_links = job.find_elements(By.TAG_NAME,'a')
            for a in all_links:
                if str(a.get_attribute('href')).startswith("https://www.linkedin.com/jobs/view") and a.get_attribute('href') not in links:
                    links.append(a.get_attribute('href'))
                else:
                    pass
                # Scrolls down for job's element
                driver.execute_script("arguments[0].scrollIntoView();", job)
            
            print(f'Collecting the links in the page: {page-1}')
            # Next page
            driver.find_element(By.XPATH, f"//button[@aria-label='Page {page}']")
            driver.execute_script("arguments[0].click();", page)
            time.sleep(3)
except:
    pass
print('Found ' + str(len(links)) + ' links for job offers')

# Create empty lists to store info about jobs
job_titles = []
company_names = []
company_locations = []
post_dates = []
work_times = []
job_desc = []

# Counters
i = 0
j = 1

# Visit each link to scrape the info
print('Visiting the links and collecting info...')
for i in range(len(links)):
    try:
        driver.get(links[i])
        i = i + 1
        time.sleep(2)
        # Click See More
        driver.find_element(By.CLASS_NAME, "artdeco-card__actions").click()
    except:
        pass

# Find general info about the job offers
contents = driver.find_element(By.CLASS_NAME, 'p5')
for content in contents:
    try:
        job_titles.append(content.find_element(By.TAG_NAME, "h1").text)
        company_names.append(content.find_element(By.CLASS_NAME, "jobs-unified-top-card__company-name").text)
        company_locations.append(content.find_element(By.CLASS_NAME, "jobs-unified-top-card__bullet").text)
        post_dates.append(content.find_element(By.CLASS_NAME, "jobs-unified-top-card__posted-date").text)
        work_times.append(content.find_element(By.CLASS_NAME, "jobs-unified-top-card__job-insight").text)
        print(f'Scraping the Job Offer {j} done.')
        j += 1
    except:
        pass
    time.sleep(5)

# Scraping the job description
job_description = driver.find_element(By.CLASS_NAME, 'jobs-description__content')
for description in job_description:
    job_text = description.find_element(By.CLASS_NAME("jobs-box__html-content").text)
    job_desc.append(job_text)
    print(f'Scraping the Job Offer {j}')
    time.sleep(2)

# Creating the dataframe
df = pd.DataFrame(list(zip(job_titles,company_names, company_locations, 
                    post_dates, work_times)),
                    columns = ['job_title', 'company_name', 
                    'company_location', 'post_date', 
                    'work_time'])

# Storing the data to csv file
df.to_csv('job_offers.csv', index = False)

# Output job descriptions to txt
with open('job_descriptions.text', 'w', encoding="uft-8") as f:
    for line in job_desc:
        f.write(line)
        f.write('\n')

driver.close()

