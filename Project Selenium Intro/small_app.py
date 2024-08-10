from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_settings=webdriver.ChromeOptions()
chrome_settings.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_settings)
driver.get("https://www.python.org/")
dates=driver.find_elements(By.CSS_SELECTOR,".event-widget .menu li time")
titles=driver.find_elements(By.CSS_SELECTOR,".event-widget .menu li a")

data_dict={}

for _ in range(len(titles)):
    data_dict[_]={
        "time":dates[_].text,
        "titles":titles[_].text
    }

print(data_dict)

driver.quit()