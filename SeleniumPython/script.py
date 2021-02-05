from selenium import webdriver 
import time
from selenium.webdriver.common.keys import Keys



driver= webdriver.Chrome("E:\Python\SeleniumPython\SeleniumPython\SeleniumPython\drivers\chromedriver.exe")
#driver = webdriver.Firefox()

driver.set_page_load_timeout(10)
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("Hello World of Automation")
driver.find_elements_by_name("btnK")[1].send_keys(Keys.ENTER)

#driver.find_element_by_xpath("//input[@type, 'submit' and @value,'Google Search'").send_keys(Keys.ENTER)
#driver.find_element_by_link_text("Google Search").send_keys(Keys.ENTER)
#driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
#driver.find_element_by_css_selector(".gNO89b").send_keys(Keys.ENTER)
#driver.find_element_by_xpath("//div[@class='gNO89b']//input[@type='submit' and @value= 'Google Search']").send_keys(Keys.ENTER)

time.sleep(4)
driver.quit()






