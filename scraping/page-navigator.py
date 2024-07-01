# page_navigator.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class PageNavigator:
    def __init__(self, driver):
        self.driver = driver

    def navigate_pages(self):
        pagination_xpath = '/html/body/div/main/section[2]/div/div/div/div[4]/ul'
        pagination = self.driver.find_element(By.XPATH, pagination_xpath)
        pages = pagination.find_elements(By.TAG_NAME, 'li')
        links = [page.find_element(By.TAG_NAME, 'a') for page in pages if page.find_elements(By.TAG_NAME, 'a')]
        
        for i in range(5):
            try:
                links[-2].click()
                time.sleep(5)
            except:
                print('Button disabled')
                break
