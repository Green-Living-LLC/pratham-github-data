# main.py
import os
from scraper import Scraper
from page_navigator import PageNavigator
from link_extractor import LinkExtractor
from pdf_downloader import PDFDownloader
from utils import setup_driver, create_folder
from config import BASE_URL, OUTPUT_DIR

def main():
    driver = setup_driver()
    scraper = Scraper(driver)
    navigator = PageNavigator(driver)
    extractor = LinkExtractor()
    downloader = PDFDownloader()

    try:
        scraper.navigate_to_page(BASE_URL)
        navigator.navigate_pages()
        
        table_html = scraper.get_table_html()
        product_links = extractor.extract_product_links(table_html)
        
        for url, product_name in product_links:
            scraper.navigate_to_page(url)
            pdf_links_html = scraper.get_pdf_links_html()
            pdf_links = extractor.extract_pdf_links(pdf_links_html)
            
            folder_path = create_folder(OUTPUT_DIR, product_name)
            downloader.download_pdfs(pdf_links, folder_path, product_name)
    
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
