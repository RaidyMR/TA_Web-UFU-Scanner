from selenium.webdriver.common.by import By
from utils.utils import get_driver

def get_file_upload_urls(main_url, visited_urls=[], file_upload_urls=[]):
    if main_url in visited_urls:
        return

    visited_urls.append(main_url)
    driver = get_driver()
    driver.get(main_url)

    links = driver.find_elements(By.TAG_NAME, "a")
    for link in links:
        href = link.get_attribute('href')
        if href is not None and href.startswith('http'):
            get_file_upload_urls(href, visited_urls=visited_urls, file_upload_urls=file_upload_urls)
            

    forms = driver.find_elements(By.TAG_NAME, "form")
    for form in forms:
        if driver.find_element(By.XPATH, "//input[@type='file']"):
            action = form.get_attribute('action')
            if action is not None:
                file_upload_urls.append(action)
            if action is None:
                file_upload_urls.append(main_url)

    driver.quit()
