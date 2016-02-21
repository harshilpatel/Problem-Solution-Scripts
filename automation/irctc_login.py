from selenium import webdriver
from selenium.webdriver.common.keys import Keys

username = ''
password = ''
captcha = ''
from_station = 'MUMBAI CENTRAL - BCT'
to_station = 'ANAND JN - ANND'
date = '05-02-2016'

if username == '' or password == '':
	username = input('Please enter username: ')
	password = input('Please enter username: ')

passenger_list = []

def clickandwait(element):
	driver.find_element_by_name(element).click()
	pass

def fill_this_name(element,value):
	username = driver.find_element_by_name(element)
	username.send_keys(value)
	pass

driver = webdriver.Chrome()
driver.get("http://www.irctc.co.in")

fill_this_name('j_username',username)
fill_this_name('j_password',password)
fill_this_name('j_captcha',input('Whats the captcha: '))
clickandwait('submit')

print("Logging in... waiting for page refresh")

fill_this_name('jpform:fromStation','MUMBAI CENTRAL - BCT')
fill_this_name('jpform:toStation', to_station)
fill_this_name('jpform:journeyDateInputDate',date)
clickandwait('jpform:jpsubmit')

# driver.close()