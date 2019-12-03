# YouTube Ad Research

## Background

This project was sparked for me when a YouTuber that goes by the name of _David Dobrick_ disclosed how much he makes from YouTube on a monthly basis from ads alone. With that number being incredibly small (~$24,000 a year) compared to back in 2013 when he was recieving more than $275,000 a month for less views on his videos. From this I was curious how accountable YouTube has been with his videos, the following research question was proposed...

### **Does YouTube Actually Serve Demonitized Videos with No Ads on their Platform?**

My goal is to essentially perform webscraping techniques in order to make sure YouTube isn't just pocketing profit off of demonitized videos while serving them ads at the same time. Since I have been watching YouTube videos with an adblocker on, I was unsure of the answer to this question. However, I knew the methods needed in order to find out.

## Method

Using a python package: `selenium` & `chromedriver` I knew I could load up an anonymous chrome brower in order to web scrape YouTube's platform. I didn't want any previous user details to play any influence in potential ad delivery methods so this method would be perfect since `selenium` loads up a fresh version of chrome on launch every time.

With the webscraping technique out of the way, I knew I wanted to webscrape a YouTuber known as _Graham Stephan_ as well. This was becuase he had very YouTube friendly content and had also disclosed how much money he makes a month from YouTube ads.

## Results

To start out, this project isn't fully completed yet. It still has some bugs that are restricting proper results to be shown. However, with the scripts that have been created so far, according to the following image, we can see that comparing these two YouTubers, we see that David's videos are getting served 0 video ads while Graham's are.

<img src="./img/ad_sum_by_user.jpg" alt="Video Ad Sum by User" width="250">
<img src="./img/num_records_by_user.jpg" alt="Number of Records by User" height="466">
<img src="./img/percentage_video_ads_by_user.jpg" alt="Number of Records by User" width="250">

## Conclusion

From these results, we can see that YouTube in fact has done their due dilligence. None of David's 30 videos that were scraped were found to have ads of any kind. Whereas Graham's 100+ videos that were scraped, just over 25% of them were found to have video ads attached at the beginning of the video.

Note that these numbers will probably change once the bugs within issues are all fixed, however, I have a strong confidence that David's numbers will stay at 0 even after they are fixed.
