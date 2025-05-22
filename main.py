from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


def fetch_bing_image_urls(query, max_results=3):
    # PATHS: Update these
    chromedriver_path = "chromedriver-linux64/chromedriver"
    chrome_binary_path = "chrome-linux64/chrome"

    # Set Chrome options
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.binary_location = chrome_binary_path

    # Start driver
    driver = webdriver.Chrome(service=Service(chromedriver_path), options=options)
    search_url = f"https://www.bing.com/images/search?q={query.replace(' ', '+')}"
    driver.get(search_url)
    time.sleep(2)

    # Grab image elements
    img_elements = driver.find_elements(By.CSS_SELECTOR, "img.mimg")
    image_urls = []

    for img in img_elements:
        src = img.get_attribute("src")
        if src and "http" in src:
            image_urls.append(src)
        if len(image_urls) >= max_results:
            break

    driver.quit()
    return image_urls

# Example usage
if __name__ == "__main__":
    query = input("Enter search query: ")
    urls = fetch_bing_image_urls(query)
    for i, url in enumerate(urls, 1):
        print(f"Image {i}: {url}")
