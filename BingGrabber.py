from selenium import webdriver
import time
import csv
from itertools import zip_longest

description = []
Links = [] 
searchstring = "Anything you Like HERE"
browser = webdriver.Chrome(executable_path="chromedriver")
url = "https://www.bing.com"
browser.get(url)
browser.maximize_window()
 
search_bar = browser.find_element_by_xpath("//*[@id='sb_form_q']")
search_bar.send_keys(searchstring)
 
search_button = browser.find_element_by_xpath("//*[@id='sb_form']/label")
search_button.click()
time.sleep(2)
for i in range(1,11):
    time.sleep(2)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    search_results = browser.find_elements_by_xpath("//*[@id='b_results']/li[@class = 'b_algo']/h2/a")

    for result in search_results:
        description.append(str(result.text))
    urls = []
    for result in search_results:
        urls.append(result.get_attribute("href"))
    for url in urls:
        Links.append(str(url))
        
    nextpage_button = browser.find_element_by_xpath('//*[@id="b_results"]/li/nav/ul/li/a[@class="sb_pagN sb_pagN_bp b_widePag sb_bp "]')
    nextpage_button.click()
browser.quit()
 
d = [description, Links]
export_data = zip_longest(*d, fillvalue = '')
with open('binglinks.csv', 'w', newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Description", "Links"))
      wr.writerows(export_data)
myfile.close()