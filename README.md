# Web-Image-Scraper

This easy-to-use Python script can be used to search for and download images from google or other search engines.

 ## Prerequisites
 * ```pip install selenium```
 * Download and install [WebDriver for Chrome](https://chromedriver.chromium.org/downloads) (win32 works for both 32-bit and 64-bit windows OS)
 * ```pip install Pillow```

 ## Edit and set the following variables in the script 🖊️
 * ```DRIVER_PATH``` - define the path to the downloaded ChromeDriver
 * ```wd.get('search_engine')``` - choose search engine 
 * ```scrape_images function``` - define the folder path for the downloaded images
 * ```gs = GoogleScraper(wd, 100)``` - state the number of images to be downloaded
 * ```gs.scrape_images('new folder name')``` - name the new folder

 ## Sample Screenshots
 
![Annotation 2021-11-17 152232](https://user-images.githubusercontent.com/75077076/143719743-d4965897-b43b-448a-93fc-11f51f2fd6c2.png)
 
 Images shown in local storage
 
![Annotation 2021-11-27 202641](https://user-images.githubusercontent.com/75077076/143719755-75523054-2a98-41fd-b8de-e89d817c055c.png)

.

.

.
#### ©️ CTTO: [Rubik's Code](https://rubikscode.net/2021/06/21/scraping-images-with-python/)
