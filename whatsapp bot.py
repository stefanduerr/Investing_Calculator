from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options() 
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)


driver.get('https://www.youtube.com/watch?v=5hr0IdVM7Qg')

# name = input('Enter the name of user or group : ') # ichselba
msg = input('Enter the message : ')
# count = int(input('Enter the count : '))

#Scan the code before proceeding further
input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//input[@id="search"]')
user.click()
user.send_keys(msg)

exe = driver.find_element_by_xpath('//button[@id="search-icon-legacy"]')
exe.click()
# user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))

# user = driver.find_element_by_id('placeholder-area')
# user.click()

# # msg_box = driver.find_element_by_class_name('p3_M1')

# msg_box = driver.find_element_by_xpath('//yt-formatted-string[@id = "contenteditable-textarea"]')
# msg_box.send_keys(msg)
# driver.find_element_by_xpath('//tp-yt-paper-button[@id = "button"]').click()

# for i in range(count):
#     msg_box.send_keys(msg)
#     driver.find_element_by_class_name('_3HQNh').click()