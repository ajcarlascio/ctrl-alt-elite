from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import datetime
import time
import boto3
 
#def lambda_handler(file_name, bucket, object_name=None):

ACCESS_KEY = 'AKIATNXFI3X6Q6ATU7O6'
SECRET_KEY = '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'

# using selenium headlessly
options = Options()
options.headless = True
s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

# installing chrome driver
driver = webdriver.Chrome(options=options)
actions = ActionChains(driver)
x = str(datetime.datetime.now())

# getting the url and saving the screenshot
driver.get('https://www.youtube.com/watch?v=VjvqGR3wsIs&ab_channel=VisitLaramie')
nav = driver.find_element(By.ID,'title')
driver.find_element(By.ID,'container').click()
actions.move_to_element_with_offset(nav, 0, 0)
time.sleep(5)
driver.save_screenshot(x +' screenshot.png')

pngOpen = x +' screenshot.png'

(left, upper, right, lower) = (120, 180, 1480, 919)
pngOpen = Image.open(x +' screenshot.png')
pngOpen = pngOpen.crop((left, upper, right, lower))
pngOpen.save(x +' screenshot.png')

s3.upload_file(
     Filename="/Users/acarlasc/Projects/ctrl-alt-elite/"+ x +" screenshot.png",
     Bucket="ctrl-alt-elite",
     Key= x +" screenshot.png"
 )

# closing driver
time.sleep(1)
driver.quit()
