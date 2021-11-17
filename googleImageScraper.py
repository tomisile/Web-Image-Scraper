# Import packages

import selenium
from selenium import webdriver
import requests
import shutil
import hashlib
import os
import io
import time
from PIL import Image

# Define the path to chrome driver
DRIVER_PATH = 'Path' # e.g. 'C:\\Users\\Username\\chromedriver_win32\\chromedriver'
wd = webdriver.Chrome(executable_path = DRIVER_PATH)
# This searches images from google.com
wd.get('https://google.com')

# Create the scraper class
class GoogleScraper():
    '''Downloades images from google based on the query.
       webdriver - Selenium webdriver
       max_num_of_images - Maximum number of images that we want to download
    '''
    def __init__(self, webdriver:webdriver, max_num_of_images:int):
        self.wd = webdriver
        self.max_num_of_images = max_num_of_images

    def _scroll_to_the_end(self):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)  

    def _build_query(self, query:str):
        return f"https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={query}&oq={query}&gs_l=img"

    def _get_info(self, query: str):
        image_urls = set()

        wd.get(self._build_query(query))
        self._scroll_to_the_end()

        # img.Q4LuWd is the google tumbnail selector
        thumbnails = self.wd.find_elements_by_css_selector("img.Q4LuWd")

        print(f"Found {len(thumbnails)} images...")
        print(f"Getting the links...")

        for img in thumbnails[0:self.max_num_of_images]:
            # We need to click every thumbnail so we can get the full image.
            try:
                img.click()
            except Exception:
                print('ERROR: Cannot click on the image.')
                continue

            images = wd.find_elements_by_css_selector('img.n3VNCb')
            time.sleep(0.3)

            for image in images:
                if image.get_attribute('src') and 'http' in image.get_attribute('src'):
                    image_urls.add(image.get_attribute('src'))

        return image_urls

    def download_image(self, folder_path:str, url:str):
        try:
            image_content = requests.get(url).content

        except Exception as e:
            print(f"ERROR: Could not download {url} - {e}")

        try:
            image_file = io.BytesIO(image_content)
            image = Image.open(image_file).convert('RGB')
            file = os.path.join(folder_path,hashlib.sha1(image_content).hexdigest()[:10] + '.jpg')

            with open(file, 'wb') as f:
                image.save(f, "JPEG", quality=85)
            print(f"SUCCESS: saved {url} - as {file}")

        except Exception as e:
            print(f"ERROR: Could not save {url} - {e}")

    def scrape_images(self, query:str, folder_path= 'path' #e.g. 'C:\\Users\\Username\\web_scrape'):
        folder = os.path.join(folder_path,'_'.join(query.lower().split(' ')))

        if not os.path.exists(folder):
            os.makedirs(folder)

        image_info = self._get_info(query)
        print(f"Downloading images...")

        for image in image_info:
            self.download_image(folder, image)

# Run scrape command
gs = GoogleScraper(wd, 100)
gs.scrape_images('fufu meal')