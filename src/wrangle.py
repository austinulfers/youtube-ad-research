import pandas as pd
import numpy as np
import os
import time
import re
from datetime import datetime, date
import json
from read_input import get_input
from json_stacked import decode_stacked

cwd = os.path.dirname(__file__)
input_fp = os.path.join(cwd, '../tools/input.txt')

def sub_desc_to_int(desc):
    desc_num = desc.replace(' subscribers', '')
    multiplier_char = desc_num[-1]

    if (multiplier_char == 'M'):
        desc_num = desc_num.replace('M', '')
        desc_num = int(float(desc_num) * 1000000)
        return desc_num
    elif (multiplier_char == 'K'):
        desc_num = desc_num.replace('K', '')
        desc_num = int(float(desc_num) * 1000)
        return desc_num
    else:
        desc_num = int(desc_num)
        return desc_num

def split(word):
    return [char for char in word]

def sum_ads(desc):
    desc_arr = split(desc)
    try:
        for char in desc_arr:
            try:
                int(char)
                desc_arr[desc_arr.index(char)] = int(char)
            except ValueError:
                desc_arr[desc_arr.index(char)] = ''
        while('' in desc_arr):
            desc_arr.remove('')
        return max(desc_arr)
    except ValueError:
        return 0

if __name__ == "__main__":

    pd_columns = [
        #all are imported as string
        'current_date',
        'user_name',
        'sub_count_desc',
        'panel_ad_title',
        'panel_ad_href',
        'video_ad_length_desc',
        'video_ad_video_desc',
        'video_ad_href',
        'ad_reasons',
        'video_title',
        'video_upload',
        'video_views',
        'video_likes',
        'video_dislikes',
        'video_comments',
        'video_duration',

        #all columns below are calculated in this script
        'sub_count_int', #int
        'video_ad_sum', #int
        'video_views_int', #int
        'video_likes_int', #int
        'video_dislikes_int', #int
        'video_comments_int' #int
    ]

    data_df = pd.DataFrame(columns = pd_columns)

    data_fn = get_input(input_fp, 1)
    data_fp = os.path.join(cwd, '../build/' + data_fn)
    data_textIO = open(data_fp, 'r')
    data_str = data_textIO.read()
    data_arr = []
    for dt in decode_stacked(data_str):
        data_df = data_df.append(pd.Series([
            dt['user_metrics']['current_date'],
            dt['user_metrics']['user_name'],
            dt['user_metrics']['sub_count_desc'],
            dt['ad_metrics']['panel_ad']['title'],
            dt['ad_metrics']['panel_ad']['href'],
            dt['ad_metrics']['video_ad']['length_desc'],
            dt['ad_metrics']['video_ad']['video_duration'],
            dt['ad_metrics']['video_ad']['href'],
            str(dt['ad_metrics']['ad_reasons']).strip('[]'),
            dt['video_metrics']['video_title'],
            dt['video_metrics']['video_upload'],
            dt['video_metrics']['video_views'],
            dt['video_metrics']['video_likes'],
            dt['video_metrics']['video_dislikes'],
            dt['video_metrics']['video_comments'],
            dt['video_metrics']['video_duration'],
            sub_desc_to_int(dt['user_metrics']['sub_count_desc']),
            sum_ads(dt['ad_metrics']['video_ad']['length_desc']),
            int(re.sub("[^0-9]", "", dt['video_metrics']['video_views'])),
            int(re.sub("[^0-9]", "", dt['video_metrics']['video_likes'])),
            int(re.sub("[^0-9]", "", dt['video_metrics']['video_dislikes'])),
            int(re.sub("[^0-9]", "", dt['video_metrics']['video_comments'])),
        ], index = data_df.columns), ignore_index = True)
    output_fp = os.path.join(cwd, '../build/' + get_input(input_fp, 2))
    data_df.to_excel(output_fp, header = True)