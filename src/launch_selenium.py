from selenium import webdriver
import os

#Returns a driver selenium chromedriver obj
def get_chromedriver(driver_path, download_path):
    """Open Selenium ChromeDriver"""
    options = webdriver.ChromeOptions()
    prefs = {'download.default_directory' : os.path.dirname(os.path.join(os.path.dirname(__file__), download_path))}
    options.add_experimental_option('prefs', prefs)
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--test-type')
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(executable_path = os.path.join(os.path.dirname(__file__), driver_path), options = options)
    return driver

if __name__ == '__main__':
    get_chromedriver('../tools/chromedriver.exe', '../build/')
    
