from selenium import webdriver
from selenium.common.exceptions import *
import os
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from launch_selenium import get_chromedriver
from read_input import get_input
import time
import re
from datetime import datetime

cwd = os.path.dirname(__file__)
input_fp = os.path.join(cwd, '../tools/input.txt')


if __name__ == "__main__":
    driver = get_chromedriver('../tools/chromedriver.exe', '../build/')
    driver.get(get_input(input_fp, 0))

    driver.implicitly_wait(5)
    # "all_html": driver.find_element_by_xpath('//*[@id="player-overlay:g"]').get_attribute('outerHTML'),
    ad_info = {
        "panel_ad": {
            "title" : driver.find_element_by_class_name('ytp-flyout-cta-headline').get_attribute('outerHTML').text,
            "href" : driver.find_element_by_class_name('ytp-flyout-cta-description').get_attribute('outerHTML').text
        },

        "video_ad" : {
            "length_desc" : driver.find_element_by_class_name('ytp-ad-simple-ad-badge').text,
            "video_duration" : driver.find_element_by_class_name('ytp-time-duration').text,
            "href" : driver.find_element_by_class_name('ytp-ad-button-text').get_attribute('outerHTML').text
        }
    }

    print(ad_info)

