import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pyvirtualdisplay import Display # for server
from fastapi import Depends
from sqlalchemy.orm import Session

from src.models import Post
from src.database import get_db


USE_GUI = False # use true ONLY FOR DEBUGGIN ON YOUR LOCAL PC


def get_firefox_driver(user_agent=None, proxy_data=None):
    """
    Configure driver for Firefox
    """
    
    options = webdriver.FirefoxOptions()
    if not USE_GUI:
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage') # disable the shared memory feature. This feature can cause memory leaks in certain situations.
    if user_agent:
        options.add_argument('--user-agent=%s' % user_agent)
    
    
    driver = webdriver.Firefox(options=options)
    return driver


class XcomParser():
    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.base_url = "https://x.com/"
        self.db = db

        self.driver = get_firefox_driver()
        self.driver.get(self.base_url)
        self.driver.set_page_load_timeout(15)


    def parse(self, account_names: str):
        # TODO
        posts = []
        for account_name in account_names:
            #self.driver.get(self.base_url + '/' + account_name)
            try:
                self.driver.get("https://x.com/ufc")
            except TimeoutException:
                print(f"Page {self.driver.current_url} is not loaded completely. Analyze current content")
        return len(posts)



if __name__ == '__main__':
    parser = ChinaNewsParser