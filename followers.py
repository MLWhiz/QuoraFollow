
# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def create_number(textdata):
    try:
        return int(textdata)
    except:
        return float(textdata[:-1])*1000


# Put your own username here
URL = "https://www.quora.com/username/followers"

browser = webdriver.Firefox()
browser.get(URL) 
time.sleep(5)

form = browser.find_element_by_class_name('form_inputs')
username = form.find_element_by_name('email')
# Insert Quora username
username.send_keys('uname')

password = form.find_element_by_name('password')
# Insert Quora Password
password.send_keys('pword')
password.send_keys(Keys.RETURN)
time.sleep(5)

followers_per_page = 10

browser.get(URL)

# get the followers count
prim_item = browser.find_elements_by_class_name("secondary")[0].find_elements_by_class_name("list_count")
time.sleep(3)
followers_count=int(prim_item[0].text.replace(",",""))
print "Number of Followers: " + str(followers_count)

# scroll down the page iteratively with a delay
for j in xrange(0, followers_count/followers_per_page + 1):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
    
options=browser.find_elements_by_class_name("pagedlist_item")

user_follower_dict = {}
for i,option in enumerate(options):
    try:
        user_follower_dict[option.find_element_by_class_name("user").get_attribute("href")+" | "+option.find_element_by_class_name("user").text+" | "+option.find_element_by_class_name("count").text] = create_number(option.find_element_by_class_name("count").text)
    except:
        pass

from collections import Counter
d = Counter(user_follower_dict)

# Print top 50 followers
for k, v in d.most_common(50):
    print '%s' % (k)