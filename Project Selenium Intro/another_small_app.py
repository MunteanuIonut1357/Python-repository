from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_settings=webdriver.ChromeOptions()
chrome_settings.add_experimental_option("detach",True)

chrome_settings.add_argument("--disable-search-engine-choice-screen")

driver=webdriver.Chrome(options=chrome_settings)
driver.get("https://secure-retreat-92358.herokuapp.com/")

text_bar=driver.find_element(By.NAME,"fName")
text_bar.send_keys("Munteanu")
text_bar=driver.find_element(By.NAME,"lName")
text_bar.send_keys("Ionut")
text_bar=driver.find_element(By.NAME,"email")
text_bar.send_keys("nutuzero1@yahoo.com")

sign_button=driver.find_element(By.CSS_SELECTOR,".btn-primary")
sign_button.click()
