from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
from bs4 import BeautifulSoup
import requests
from splinter import Browser
from urllib.parse import urlsplit
import os 
import time





def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrape_info():
    browser = init_browser()

    # Visit https://mars.nasa.gov/news/"
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)




    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    
    # 1-NASA Mars News
    news_title = soup.find('div',class_='content_title').text
    news_p = soup.find('div',class_='article_teaser_body').text


    # 2-JPL Mars Space Images - Featured Image (scrap the image url)
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
   
    image_url = soup.find('article')['style']
    image_url1 = image_url.replace("background-image: url('","")
    image_url2 = image_url1.replace("');","")
    img_path = 'https://www.jpl.nasa.gov'
    space_img = img_path + image_url2
   


    #  3- Mars Weather
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    weather = soup.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text
    mars_weather = weather.replace("hPapic.twitter.com/8SrPjAhpGZ","")


    # 4- Mars Facts

    url = "https://space-facts.com/mars/"
    tables = pd.read_html(url)
    df = tables[0]
    df.columns = ['', 'value']
    df.set_index('', inplace=True)
    html_table = df.to_html()
    html_table_clean = html_table.replace("\n","")
    html_table_clean 
    
    
    






    # Store data in a dictionary
    mars_news = {
        "news_title":news_title,
        "news_p":news_p,
        "space_img":space_img,
        "mars_weather":mars_weather,
        "html_table_clean":html_table_clean , 
    }


    
    
    

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_news




























# 3- Mars Weather
    #url = 'https://twitter.com/marswxreport?lang=en'

# 4- Mars Facts
    #url = "https://space-facts.com/mars/"

# 5- Mars Hemispheres
    #url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'