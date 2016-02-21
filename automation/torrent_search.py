from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main():
	try:
		to_search = input("Enter keyworks to search")
		driver = webdriver.Chrome()
		driver.get('http://www.thepiratebay.se')
		a = driver.find_element_by_name('q')
		a.send_keys(to_search)
		driver.find_element_by_xpath('//input[@title="Pirate Search"]').click()
		print('Redirecting')
	except Exception as e:
		print(e)



if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		print(e)