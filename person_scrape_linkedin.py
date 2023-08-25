# Importing necessary tools for our program.

import csv  # Helps us work with files that have rows and columns, like a spreadsheet.
from selenium import webdriver  # A tool that lets our program use a web browser, just like when you go on the internet.
from linkedin_scraper import Person, actions, Company  # Special tools to grab info from LinkedIn, a website for job professionals.
from selenium.webdriver.chrome.service import Service as ChromeService  # This helps us set up and control the Chrome browser.
from webdriver_manager.chrome import ChromeDriverManager  # Helps us get the latest version of the Chrome browser.
import time, pickle  # 'time' lets us pause our program, 'pickle' lets us save and load data easily.
from selenium.webdriver.chrome.options import Options  # Gives us extra settings for the Chrome browser.
from selenium.common.exceptions import WebDriverException  # Helps us deal with browser-related errors.

def person_scrape(link, driver):
    # Grab details about a person from LinkedIn.
    
    person = Person(link, driver=driver, scrape=False)  # Prepare to get person's details.
    time.sleep(10)  # Wait for 10 seconds. Sometimes we wait so websites don't get mad at us.
    person.scrape(close_on_complete=False)  # Now, get the person's details.
    
    # Store the information we found in different boxes (or variables).
    name = person.name
    title = person.job_title
    now_company = person.company
    experience = person.experiences
    current_company = experience[0]
    link_to_company = current_company.linkedin_url
    location = current_company.location
    about_person=person.about
    
    time.sleep(7)  # Another short wait.
    
    company = Company(link_to_company, driver=driver, close_on_complete=False, get_employees=False)  # Prepare to get company's details.
    company_size = company.company_size
    company_website = company.website
    about_company = company.about_us
    
    list=[name, title, about_person, now_company, link_to_company, location]  # Pack the details we got into a list.
    return list

def company_scrape(link_to_company, driver):
    # Grab details about a company from LinkedIn.
    
    company = Company(link_to_company, driver=driver, close_on_complete=False)  # Prepare to get company's details.
    company_size = company.company_size
    company_website = company.website
    about = company.about_us
    
    list=[company_size, company_website, about]  # Pack the details we got into a list.
    return list

options = Options()
options.add_argument("user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 3")  # Special settings for our browser.

new_data=[]  # An empty box to keep the details we find.
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)  # Start our browser.

# Reading a file with lots of LinkedIn profiles and gathering their details.
i=0
with open(r'C:\Users\User\Downloads\Telegram Desktop\consulting_profiles1(1-103).csv', 'r', encoding='utf8') as file:
    reader=csv.reader(file)  # Open our file and get ready to read.
    data=list(reader)  # Read everything inside.
    
    # Go through each row in the file.
    for row in data:
        try:
            person_info=person_scrape(row[0], driver)  # Get details for the person in this row.
            row.extend(person_info)  # Add those details to our current row.
            i+=1
            new_data.append(row)  # Add the completed row to our 'new_data' box.
            print('new person', i)
            
            # Sometimes we pause for a bit, either for a short or a longer time.
            if i % 5 == 0:
                time.sleep(30)
            else:
                time.sleep(7)
        except WebDriverException as e:  # If our browser has a hiccup, tell us what went wrong.
            print(e)
            pass
        except Exception as e:  # If anything else goes wrong, also tell us.
            print(e)
            pass

# If we suddenly stop the program, try to save our 'new_data' safely.
except KeyboardInterrupt:
    try:
        with open('emergency_save_person_data.pickle', 'wb') as file:
            pickle.dump(new_data, file)
    except:
        pass

# Save all the details we've gathered.
try:
    with open('person_data.pickle', 'wb') as file:
        pickle.dump(new_data, file)
except:
    pass

# Write the new data into a new CSV file.
try:
    with open('talent_linkedin.csv', 'w', encoding="utf-8", newline='') as file:
        writer=csv.writer(file)
        writer.writerows(new_data)
        print(new_data)
except:
    print(new_data)

# Save the original data as a backup.
try:
    with open('linkedin_consulting_extra_save.csv', 'w', encoding="utf-8", newline='') as file:
        writer=csv.writer(file)
        writer.writerows(data)
        print(data)
except:
    print(data) 
