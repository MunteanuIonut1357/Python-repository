import time

from selenium import webdriver
from selenium.webdriver.common.by import By

INDEX = 10
PRODUCT_INDEX = 1

chrome_settings = webdriver.ChromeOptions()
chrome_settings.add_experimental_option("detach", True)

chrome_settings.add_argument("--disable-search-engine-choice-screen")

driver = webdriver.Chrome(options=chrome_settings)
driver.get("https://orteil.dashnet.org/cookieclicker/")

Consent_Button = driver.find_element(By.CSS_SELECTOR, ".fc-button-label")
Consent_Button.click()

time.sleep(1)

Language_Button = driver.find_element(By.CSS_SELECTOR, "#langSelect-EN")
Language_Button.click()

time.sleep(1)

Big_cookie = driver.find_element(By.CSS_SELECTOR, "#bigCookie")

Cookie_text = driver.find_element(By.CSS_SELECTOR, "#cookies")

Dict_Products = {
    "#product0": "#productPrice0",
}

input("Press start:")

while True:

    Cookie_number = int(Cookie_text.text.split(" ")[0].replace(",", ""))

    for key, item in Dict_Products.items():

        Product_Price_raw = driver.find_element(By.CSS_SELECTOR, item)
        Product_Price = int(Product_Price_raw.text.replace(",", ""))
        # print(Cookie_number)
        # print(Product_Price)
        if Cookie_number >= Product_Price:
            Upgrade = driver.find_element(By.CSS_SELECTOR, key)

            Upgrade.click()

    if Cookie_number > INDEX:
        new_product = "#product" + str(PRODUCT_INDEX)
        new_product_price = "#productPrice" + str(PRODUCT_INDEX)

        Dict_Products[new_product] = new_product_price

        PRODUCT_INDEX += 1
        INDEX = INDEX * 11

    Old_Cookie_num = Cookie_number

    while True:
        Big_cookie.click()
        Cookie_number = int(Cookie_text.text.split(" ")[0].replace(",", ""))
        if Cookie_number > Old_Cookie_num * 1.25:
            break
