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
from datetime import datetime, date

cwd = os.path.dirname(__file__)
input_fp = os.path.join(cwd, '../tools/input.txt')


if __name__ == "__main__":
    driver = get_chromedriver('../tools/chromedriver.exe', '../build/')
    driver.get(get_input(input_fp, 0))

    driver.implicitly_wait(5)

    try:
    
        reason_html_list = driver.find_element_by_class_name('ytp-ad-info-dialog-ad-reasons')
        reason_tag_list = reason_html_list.find_elements_by_tag_name("li")
        reason_text_list = []
        for tag in reason_tag_list:
            reason_text_list.append(tag.get_attribute("innerHTML"))

        ad_metrics = {
            "panel_ad": {
                "title" : BeautifulSoup(driver.find_element_by_class_name('ytp-flyout-cta-headline').get_attribute('outerHTML'), features = "lxml").getText(),
                "href" : BeautifulSoup(driver.find_element_by_class_name('ytp-flyout-cta-description').get_attribute('outerHTML'), features = "lxml").getText()
            },

            "video_ad" : {
                "length_desc" : driver.find_element_by_class_name('ytp-ad-simple-ad-badge').text,
                "video_duration" : driver.find_element_by_class_name('ytp-time-duration').text,
                "href" : BeautifulSoup(driver.find_element_by_class_name('ytp-ad-button-text').get_attribute('outerHTML'), features = "lxml").getText()
            },

            "ad_reasons": reason_text_list
        }

        user_metrics = {
            "current_date" :  date.today(),
            "user_name" : driver.find_element_by_id('text-container').text,
            "sub_count_desc" : driver.find_element_by_id('owner-sub-count').text 
        }

        video_metrics = {
            "current_date" :  date.today(),
            "video_title" : driver.find_element_by_xpath('//*[@id="container"]/h1/yt-formatted-string').text,
            "video_upload" : driver.find_element_by_xpath('//*[@id="date"]/yt-formatted-string').text,
            "video_views" : driver.find_element_by_xpath('//*[@id="count"]/yt-view-count-renderer/span[1]').text,
            "video_likes" : driver.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[1]/a').find_element_by_id('text').get_attribute('aria-label'),
            "video_dislikes" : driver.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[2]/a').find_element_by_id('text').get_attribute('aria-label'),
            "video_comments" : driver.find_element_by_xpath('//*[@id="count"]/yt-formatted-string')
        }

        print(video_metrics)
    
    except NoSuchElementException:
        driver.find_element_by_xpath('//*[@id="movie_player"]/div[21]/div[2]/div[1]/button').click()

