from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
import datetime
import time
 
# using selenium headlessly
options = Options()
options.headless = True

# installing chrome driver
driver = webdriver.Chrome(options=options)
actions = ActionChains(driver)

x = str(datetime.datetime.now())
 
# getting the url and saving the screenshot
driver.get('https://www.youtube.com/watch?v=VjvqGR3wsIs&ab_channel=VisitLaramie')
nav = driver.find_element(By.ID,'container')
driver.find_element(By.ID,'container').click()
actions.move_to_element_with_offset(nav, 0, 0)
time.sleep(3)
driver.save_screenshot(x +' screenshot.png')

pngOpen = x +' screenshot.png'

(left, upper, right, lower) = (120, 180, 1445, 919)
pngOpen = Image.open(x +' screenshot.png')
pngOpen = pngOpen.crop((left, upper, right, lower))
pngOpen.save(x +' screenshot.png')

# closing driver
time.sleep(1)
driver.quit()
