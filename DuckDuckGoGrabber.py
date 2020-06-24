from selenium import webdriver
import time
import csv
from itertools import zip_longest

searchstring = "Anything you Like HERE"
description = []
Links = [] 
browser = webdriver.Chrome(executable_path="chromedriver")
url = "https://www.duckduckgo.com"
browser.get(url)
browser.maximize_window()
 
search_bar = browser.find_element_by_xpath("//input[@id='search_form_input_homepage']")
search_bar.send_keys(searchstring)
 
search_button = browser.find_element_by_xpath("//input[@id='search_button_homepage']")
search_button.click()
 
#search_results = browser.find_elements_by_xpath("//a[@class='result__a']")
Settings_Button = browser.find_elements_by_xpath("//a[@class = 'zcm__link dropdown__button js-dropdown-button']")[0]
Settings_Button.click()
Toggle_Button = browser.find_elements_by_xpath("//label[@for= 'setting_kav']")[0]
Toggle_Button.click()
Settings_Button.click()
SCROLL_PAUSE_TIME = 1

# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
search_results = browser.find_elements_by_xpath("//div[@id='links']/div/div/h2/a[@class='result__a']")
print(len(search_results))
for result in search_results:
    description.append(str(result.text))
    
urls = []
for result in search_results:
    urls.append(result.get_attribute("href"))
    
for url in urls:
    Links.append(str(url))
 
browser.quit()
d = [description, Links]
export_data = zip_longest(*d, fillvalue = '')
with open('duckduckgolinks.csv', 'w', newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Description", "Links"))
      wr.writerows(export_data)
myfile.close()