from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
import datetime
import time
import boto3
import os
from dotenv import load_dotenv

#create loop to simulate automation
options = Options()
options.headless = True
load_dotenv()

access = os.getenv("ACCESS_KEY")
secret = os.getenv("SECRET_KEY")
s3 = boto3.client('s3', aws_access_key_id=access, aws_secret_access_key=secret)

# installing chrome driver
driver = webdriver.Chrome(options=options)
actions = ActionChains(driver)

for i in range(10):
            
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
    jpgConvert = pngOpen.convert("RGB")
    jpgConvert.save(x +' screenshot.jpg')

    s3.upload_file(
        Filename="/Users/acarlasc/Projects/ctrl-alt-elite/"+ x +" screenshot.jpg",
        Bucket="ctrl-alt-elite-screenshots",
        Key= x +" screenshot.jpg",
        ExtraArgs={'ContentType': 'image/jpg'}
    )

    os.remove('/Users/acarlasc/Projects/ctrl-alt-elite/' + x + ' screenshot.png')
    os.remove('/Users/acarlasc/Projects/ctrl-alt-elite/' + x + ' screenshot.jpg')
    time.sleep(10)
# closing driver
time.sleep(1)
#driver.quit()
