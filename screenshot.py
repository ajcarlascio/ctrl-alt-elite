from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import datetime
import time
 
# using selenium headlessly
options = Options()
options.headless = True
 
# installing chrome driver
driver = webdriver.Chrome(options=options)

x = str(datetime.datetime.now())
 
# getting the url and saving the screenshot
driver.get('https://www.youtube.com/watch?v=VjvqGR3wsIs&ab_channel=VisitLaramie')
driver.find_element(By.ID,'container').click()
time.sleep(1)
driver.save_screenshot(x +' screenshot.png')
 
# closing driver
#driver.quit()
