
# utils.py
from undetected_chromedriver import Chrome, ChromeOptions
import os

def setup_driver():
    options = ChromeOptions()
    # options.add_argument('--headless')  # optionally run in headless mode
    return Chrome(options=options)

def create_folder(base_dir, folder_name):
    folder_path = os.path.join(base_dir, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    return folder_path

