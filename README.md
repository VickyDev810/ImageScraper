# 🖼️ Image Scraper with Selenium

A flexible Python script to scrape image URLs from **any website** using Selenium. Just plug in your target URL and CSS selector, and it will fetch image sources with a headless Chrome browser.

---

## 🚀 Features

* Headless Chrome automation
* Scrapes `<img>` tags or any image-containing elements
* Works on **any site** — just update the URL and selector
* Clean and configurable

---

## 🧰 Requirements

* Python 3.7+
* Google Chrome
* ChromeDriver (matching your Chrome version)
* Selenium

### 📦 Install dependencies

```bash
pip install selenium
```

### 🧱 Install Chrome & ChromeDriver

Use [this helper script](https://github.com/macchrome/chromium/releases) or install via package manager:

**Ubuntu/Debian:**

```bash
sudo apt install -y chromium-browser chromium-chromedriver
```

**macOS (Homebrew):**

```bash
brew install --cask google-chrome
brew install chromedriver
```

> **Note**: Make sure `chromedriver` is in your system's `PATH`. You can verify with:

```bash
which chromedriver
```

---

## ⚙️ Configuration

Update the script with your:

* Target URL
* Image CSS selector (defaults to standard `<img>` tags)

Example snippet to modify:

```python
search_url = "https://example.com/images"
img_elements = driver.find_elements(By.CSS_SELECTOR, "img")  # or your custom selector
```

---

## 🧠 Usage

Run the script:

```bash
python main.py
```

It will prompt you for a URL, open it in a headless browser, and return a list of image URLs.

Example:

```
Enter page URL: https://example.com/gallery
Image 1: https://...
Image 2: https://...
Image 3: https://...
```

---

## 🛠 Script Overview

```python
def fetch_image_urls(url, selector="img", max_results=3):
    # Your scraping logic here
```

### 🔄 Change the selector to customize scraping:

* `.photo-class img` – nested images
* `div.gallery img` – within specific containers
* `img.thumbnail` – specific class-based images

---

## 📁 Project Structure

```
.
├── main.py      # Main script
```

---

## ⚠️ Disclaimer

* Be respectful of website terms of service.
* This is for educational or authorized use only.
* Some sites may use lazy-loading or dynamic content (use `driver.execute_script()` or scroll automation if needed).

---
