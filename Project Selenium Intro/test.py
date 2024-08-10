from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_settings=webdriver.ChromeOptions()
chrome_settings.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_settings)
driver.get("https://roxanaa1.github.io/html-portfolio/")

value=driver.find_element(By.CSS_SELECTOR,"body h2")

print(value.text)

