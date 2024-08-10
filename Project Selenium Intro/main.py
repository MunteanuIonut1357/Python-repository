from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_settings=webdriver.ChromeOptions()
chrome_settings.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_settings)
driver.get("https://answear.ro/p/max-co-rochie-culoarea-bej-mini-drept-2416621013200-1266617")
price_full=driver.find_element(By.CLASS_NAME,value="ProductCard__priceSaleMinimal__WGeHM")


print(f"Price is {price_full.text.split(" ")[0]}")

driver.quit()