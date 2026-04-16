import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []
TotalAmount = []
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


options = Options()
options.binary_location =  r"C:\Users\shamila\AppData\Local\chrome\chrome.exe"

options.add_argument("start-maximized")
options.add_argument("disable-extensions")
options.add_argument("--no_sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service (r"C:\Users\shamila\AppData\Local\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)

products = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(products)
assert count>0

for product in products:

    product.find_element(By.XPATH, "div/button").click()


driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()

driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

amounts = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sumTotal = 0
for amount in amounts:
    sumTotal += int(amount.text)
print(sumTotal)

TotalAmount = int (driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sumTotal == TotalAmount


driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys('rahulshettyacademy')
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print (driver.find_element(By.CSS_SELECTOR, ".promoInfo").text)

disAmount = float (driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
assert disAmount < TotalAmount

driver.find_element(By.XPATH, "//button[text()='Place Order']").click()

dropdown_element = (driver.find_element(By.XPATH, "//select"))
dropdown_element.send_keys('p')
dropdown_element.click()
print(dropdown_element.get_attribute('value'))
driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
driver.find_element(By.XPATH, "//button[text()='Proceed']").click()




input("Press Enter to close browser...")
driver.quit()