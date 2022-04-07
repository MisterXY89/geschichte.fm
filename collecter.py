
import time
import requests
from bs4 import BeautifulSoup
# from requests_html import HTMLSession
from WavUrlFetcher import WavUrlFetcher


class PodcastScraper():

    def __init__(self, lates_episode=340):
        self.base_url = "https://www.geschichte.fm/archiv/"        
        self.latest_episode = lates_episode
        self.episode_urls = []
        self.gen_ep_urls()
        self.parser = "html.parser"
        self.wuf = WavUrlFetcher()
        self.episodes = []

    def gen_ep_urls(self):
        for x in range(2, self.latest_episode):
            if x < 10:
                self.episode_urls.append(f"{self.base_url}zs0{x}")
            if x <= 270:
                self.episode_urls.append(f"{self.base_url}zs{x}")
            if x > 270:
                self.episode_urls.append(f"{self.base_url}gag{x}")

    def get_soup(self, url):
        try:
            response = requests.get(url)
        except Exception as err:
            print(f"Error: {err}")
            print(f"WITH FOLLOWING URL: {url=}")
            raise err
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, self.parser)
            return soup

    def collect_download_links(self):
        """
        generator for finding all download links
        """
        for i, episode_u in enumerate(self.episode_urls):
            ep_download_url, ep_name, ep_description = self.wuf.collect(episode_u)
            self.episodes.append({
                "number": i,
                "url": episode_u,
                "download_link": ep_download_url,                
                "name": ep_name,
                "description": ep_description
            })
            yield ep_download_url


    def download_episodes(self):
        for ep_link in self.collect_download_links():            
            pass
            # check if worker is free and if yes, assign url 



ps = PodcastScraper()
for ep in ps.collect_download_links():
    print(ep)