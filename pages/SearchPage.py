import time

from selenium.webdriver.common.by import By

search_field = "//input[@placeholder='Search']"
search_button = '//*[@id="search"]/span/button'
result_prod = "//a[normalize-space()='HP LP3065']"



def Search_product(driver,val):
    driver.find_element(By.XPATH, search_field).send_keys(val)
    driver.find_element(By.XPATH, search_button).click()
    assert driver.find_element(By.XPATH, result_prod).is_displayed()
