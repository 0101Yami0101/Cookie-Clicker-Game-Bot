#cookie clicker game automation

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s, )
driver.get('http://orteil.dashnet.org/experiments/cookie/')

def Buy(count):
    if count > 7000:
      shipment = driver.find_element(By.ID, "buyShipment")
      shipment.click()
    elif count > 2000:
      mine = driver.find_element(By.ID, "buyMine")
      mine.click()
    elif count > 500:
      factory = driver.find_element(By.ID, "buyFactory")
      factory.click()
    elif count > 100:
      grandma = driver.find_element(By.ID, "buyGrandma")
      grandma.click()
    elif count > 50: 
      cursor = driver.find_element(By.ID, "buyCursor")
      cursor.click()

cookie = driver.find_element(By.XPATH,"//*[@id='cookie']")

current = time.time()
timeout = current + 5 #16002
while True:
  ##click on cookie
  cookie.click()

  #checking money
  money_item = driver.find_element(By.ID, "money")
  money = int(str(money_item.text).replace(",",""))

  #if 5 secs passed
  if time.time() > timeout:
    Buy(money)
    timeout = time.time() + 5
  








