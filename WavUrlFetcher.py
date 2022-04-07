
import time
#from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options

URL = "https://www.geschichte.fm/podcast/zs270/"


class WavUrlFetcher:
    def __init__(self):
        self.opts = Options()
        # self.opts.headless = True
        self.driver = webdriver.Chrome(options=self.opts) #(executable_path="/usr/lib/chromium-browser/chromedriver", options=self.opts)
        print("driver set")        

    def load_page(self, url):
        try:
            self.driver.get(url)
            time.sleep(2)
        except Exception as e:
            return str(e)
        # return page_source

    def quit(self):
        try:
            self.driver.quit()
            self.display.stop()
        except Exception as eQuit:
            return str(eQuit)

    def get_wav_url(self):
        ep_name = self.driver.find_element(By.CLASS_NAME, value="page-title").text
        ep_description = self.driver.find_element(By.CLASS_NAME, value="entry-content").text
        self.driver.switch_to.frame(self.driver.find_element(By.TAG_NAME, value="iframe"))
        episode_download_link = self.driver.find_element(
                                By.CLASS_NAME, value="share-download"
                            ).find_element(By.TAG_NAME, value="a").get_attribute("href")
        return episode_download_link, ep_name, ep_description

    def collect(self, url):
        self.load_page(url)
        episode_download_link = self.get_wav_url()
        return episode_download_link

    def restart(self):
        self.driver.quit()
        # self.display.stop()
        self.driver = webdriver.Chrome() # executable_path="/usr/lib/chromium-browser/chromedriver", options=self.opts)

# wuf = WavUrlFetcher()
# wuf.collect(URL)