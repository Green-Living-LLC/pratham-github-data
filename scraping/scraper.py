
# scraper.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Scraper:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_page(self, url):
        self.driver.get(url)

    def get_table_html(self):
        table_xpath = "/html/body/div/main/section[2]/div/div/div/div[3]"
        table_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, table_xpath))
        )
        return table_element.get_attribute('outerHTML')

    def get_pdf_links_html(self):
        pdf_links_xpath = '/html/body/div/main/section[2]/div/div/div/div[3]/div'
        pdf_links_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, pdf_links_xpath))
        )
        return pdf_links_element.get_attribute('outerHTML')

