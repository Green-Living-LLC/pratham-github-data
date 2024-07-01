
# link_extractor.py
from bs4 import BeautifulSoup

class LinkExtractor:
    def extract_product_links(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        initial_links = soup.find_all('a', href=True)
        links = [('https://c2ccertified.org' + link['href'], 
                  link.find('span', class_='listinline__title').text) 
                 for link in initial_links]
        return [(link[0], '_'.join(link[1].lower().split())) for link in links]

    def extract_pdf_links(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        pdfs = soup.find_all('div', class_='crosslink crosslink--card crosslink--light u-aspect-box')
        pdf_links = [(pdf.find('div', class_='crosslink__body').text, 
                      pdf.find('a', href=True)['href']) 
                     for pdf in pdfs]
        return [(text.lower().replace(' ', '_').replace('/', '_').replace('(', '').replace(')', ''), link) 
                for text, link in pdf_links]
