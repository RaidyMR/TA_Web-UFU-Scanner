import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

def get_driver():   
    user_agent = os.getenv("USER_AGENT")

    options = ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)

    return driver

def is_vulnerable(text, status_code):
    if "File upload harus berupa gambar!" in text \
    or "Anda mau ngehack ya?" in text \
    or "Upload gagal!" in text \
    or status_code != 200:
        return False
    
    return True

# def delete_modified_files():
