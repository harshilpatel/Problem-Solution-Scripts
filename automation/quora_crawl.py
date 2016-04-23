from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,math
def main():
	try:
		to_search = input("Enter Topic: ")
		driver = webdriver.Chrome()
		driver.get('http://www.quora.com/'+ to_search)
		a = driver.find_element_by_name('q')
		a.send_keys(to_search)
		# driver.find_element_by_xpath('//input[@title="Pirate Search"]').click()
		start = time.time()
		while int(math.fabs(time.time() - start) < 50):
			driver.execute_script("window.scrollTo(0, 1000);")
			# driver.find_element_by_classname("read_more").click()
		print('Done')
	except Exception as e:
		print(e)



if __name__ == '__main__':
	main()