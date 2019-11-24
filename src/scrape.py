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
import json

cwd = os.path.dirname(__file__)
input_fp = os.path.join(cwd, '../tools/input.txt')

def get_metrics(driver, option):
    """Returns dict of metrics of specfied option
    
    Arguments:
        driver {webdriver} -- Chrome environment
        option {string} -- 'ad', 'user', or 'video'

    Raises: 
        NameError -- when invalid 'option' is passed
    
    Returns:
        dict -- metrics of different options
    """
    if option == 'ad':
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
        return ad_metrics

    elif option == 'user':
        user_metrics = {
            "current_date" :  datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
            "user_name" : driver.find_element_by_id('text-container').text,
            "sub_count_desc" : driver.find_element_by_id('owner-sub-count').text 
        }
        return user_metrics
    
    elif option == 'video':
        driver.execute_script("window.scrollTo(0, 500)")
        duration_html = driver.find_elements_by_xpath('//*[@id="overlays"]/ytd-thumbnail-overlay-time-status-renderer/span')
        duration_text = []
        for i in duration_html:
            duration_text.append(i.text)
        current_video_index = int(driver.find_element_by_xpath('//*[@id="publisher-container"]/div/yt-formatted-string').text.split(' ')[0])
        video_metrics = {
            "current_date" :  datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
            "video_title" : driver.find_element_by_xpath('//*[@id="container"]/h1/yt-formatted-string').text,
            "video_upload" : driver.find_element_by_xpath('//*[@id="date"]/yt-formatted-string').text,
            "video_views" : driver.find_element_by_xpath('//*[@id="count"]/yt-view-count-renderer/span[1]').text,
            "video_likes" : driver.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[1]/a').find_element_by_id('text').get_attribute('aria-label'),
            "video_dislikes" : driver.find_element_by_xpath('//*[@id="top-level-buttons"]/ytd-toggle-button-renderer[2]/a').find_element_by_id('text').get_attribute('aria-label'),
            "video_comments" : driver.find_element_by_xpath('//*[@id="count"]/yt-formatted-string').text,
            "video_duration" : duration_text[current_video_index - 1]
        }
        driver.execute_script("window.scrollTo(0, -500)")
        return video_metrics
    
    else:
        raise NameError()


if __name__ == "__main__":
    driver = get_chromedriver('../tools/chromedriver.exe', '../build/')
    driver.get(get_input(input_fp, 0))

    driver.implicitly_wait(5)

    user_metrics = get_metrics(driver, 'user')
    
    ad_metrics = get_metrics(driver, 'ad')
    video_metrics = get_metrics(driver, 'video')

    all_metrics = {
        "user_metrics" : user_metrics,
        "ad_metrics" : ad_metrics,
        "video_metrics" : video_metrics
    }

    all_metrics_json = json.dumps(all_metrics)
    print(all_metrics_json)
    output_fp = '../build/' + get_input(input_fp, 1) + '.txt'
    output_fp = os.path.join(cwd, output_fp)
    with open(output_fp, 'a', encoding = 'utf-8') as f:
        json.dump(all_metrics_json, f, ensure_ascii = False)