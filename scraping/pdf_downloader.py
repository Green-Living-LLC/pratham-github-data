
# pdf_downloader.py
import requests
import os

class PDFDownloader:
    def download_pdfs(self, pdf_links, folder_path, product_name):
        for cert_name, url in pdf_links:
            r = requests.get(url, stream=True)
            file_path = os.path.join(folder_path, f'{product_name}_{cert_name}.pdf')
            with open(file_path, 'wb') as f:
                f.write(r.content)
            print(f"Downloaded: {file_path}")
