from selenium import webdriver
import time
import csv
from itertools import zip_longest
from selenium.webdriver.common.keys import Keys

searchstring = "Anything you Like HERE"
description = []
Links = [] 
browser = webdriver.Chrome(executable_path="chromedriver")
url = "https://www.google.com"
browser.get(url)
browser.maximize_window()
 
search_bar = browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
search_bar.send_keys(searchstring)
search_bar.send_keys(Keys.RETURN)

time.sleep(2)
for i in range(1,7):
    time.sleep(2)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    search_results = browser.find_elements_by_xpath('//*[@id="rso"]/div/div/div[@class = "r"]/a')

    for result in search_results:
        description.append(str(result.text))
    urls = []
    for result in search_results:
        urls.append(result.get_attribute("href"))
    for url in urls:
        Links.append(str(url))
        
    nextpage_button = browser.find_element_by_xpath('//*[@id="pnnext"]')
    nextpage_button.click()
browser.quit()
 
d = [description, Links]
export_data = zip_longest(*d, fillvalue = '')
with open('GoogleLinks.csv', 'w', newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Description", "Links"))
      wr.writerows(export_data)
myfile.close()