from splinter import Browser
from bs4 import BeautifulSoup as bs
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

    
    # collect the first news title
    news_title = soup.find('div',class_='content_title').text
    


    # Store data in a dictionary
    mars_news = {
        "news_title":news_title,
         
    }


    
    
    

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_news


























#2-JPL Mars Space Images - Featured Image (scrap the image url)
    #url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'

# 3- Mars Weather
    #url = 'https://twitter.com/marswxreport?lang=en'

# 4- Mars Facts
    #url = "https://space-facts.com/mars/"

# 5- Mars Hemispheres
    #url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'