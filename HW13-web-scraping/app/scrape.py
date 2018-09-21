#!/opt/anaconda3/bin/python
# coding: utf-8

'''
###################################################################################
# @script scrape.py                                                               #
# @version  1.0.0                                                                 #
#---------------------------------------------------------------------------------#
#                                                                                 #
# Modification History                                                            #
#                                                                                 #
# Date        Name             Description                                        #
# ----------  -----------      ----------------------------------                 #
# 2018/09/18  (chris)          Original script                                    #
#                                                                                 #
###################################################################################
'''

## Imports
import pandas as pd
import requests as req
import time, uuid
from splinter import Browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


'''
## Init Functions
-------------------------------------------------
'''
def init_chromedriver():
	# Initialize Chrome browser
	chrome_options = Options()
	chrome_options.add_argument('--headless') # Runs Chrome in headless mode.
	chrome_options.add_argument('--no-sandbox') # # Bypass OS security model
	chrome_options.add_argument('start-maximized')
	chrome_options.add_argument('disable-infobars')
	chrome_options.add_argument('--disable-extensions')

	executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
	return Browser('chrome', **executable_path, headless=False, options=chrome_options)

'''
## Functions
-------------------------------------------------
'''
def browser_soup(code):
	html = BeautifulSoup(code, "html.parser")
	return html

def mars_news(code):
	html = browser_soup(code)
	
	try:
		slide = html.find('li', class_='slide')
		news_title = slide.find('div', class_='content_title').text
		news_paragraph = slide.find('div', class_='article_teaser_body').text
	except:
		news_title = 'news title not found'
		news_paragraph = 'news paragraph not found'

	return news_title, news_paragraph 

def mars_featured_image(code):
	html = browser_soup(code)
	
	try:
		image_url = html.find('a', {'id': 'full_image', 'data-fancybox-href': True}).get('data-fancybox-href')
		featured_image_url = 'https://www.jpl.nasa.gov{}'.format(image_url)
	except:
		featured_image_url = 'featured image url not found'
		
	return featured_image_url

def mars_weather(code):
	html = browser_soup(code)

	try:
		mars_weather = html.select('#stream-items-id > li p')[0].text
	except:
		mars_weather = 'no weather found'
		
	return mars_weather

def mars_facts(url):
	mars_facts = pd.read_html(url)
	
	try:
		mars_facts_df = pd.DataFrame(mars_facts[0])
		mars_facts_df.columns = ['Description', 'Values']
		mars_facts_html = mars_facts_df.to_html(classes='table table-condensed table-hover')
		mars_facts_html = mars_facts_html.replace('\n', '')		
	except:
		mars_facts_html = '<p>no data</p>'

	return mars_facts_html

def mars_hemisphere_images(url, browser):
	browser.visit(url)
	html_code = browser.html
	html_clean = BeautifulSoup(html_code, "html.parser")

	try:
		images = html_clean.find('div', class_='collapsible results')
		hemisphere_image_urls = []

		for i in range(len(images.find_all('div', class_='item'))):
			time.sleep(5)

			image = browser.find_by_tag('h3')
			image[i].click()

			html_code = browser.html
			html_clean = BeautifulSoup(html_code, "html.parser")

			title = html_clean.find('h2', class_='title').text
			div = html_clean.find('div', class_='downloads')

			for li in div:
				link = div.find('a')

			images = { 'title' : title, 'img_url' : link.attrs['href'] }

			hemisphere_image_urls.append(images)
			browser.back()
	except:
		hemisphere_image_urls = 'no data'

	return hemisphere_image_urls


def scrape():
	browser = init_chromedriver()
	
	news_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
	featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
	weather_url = 'https://twitter.com/marswxreport?lang=en'
	facts_url = 'https://space-facts.com/mars/'
	images_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

	# mars news
	browser.visit(news_url)
	html_code = browser.html
	news_title, news_paragraph = mars_news(html_code)
	
	# featured image
	browser.visit(featured_image_url)
	html_code = browser.html
	featured_image = mars_featured_image(html_code)
	
	# weather
	browser.visit(weather_url)
	html_code = browser.html	
	weather = mars_weather(html_code)
	
	# mars facts
	facts = mars_facts(facts_url)
	
	# images
	images = mars_hemisphere_images(images_url, browser)

	mars_dict = {
        "id": str(uuid.uuid1()),
        "news_title": news_title,
        "news_body": news_paragraph,
        "featured_image": featured_image,
        "weather": weather,
        "facts": facts,
        "images": images
	}

	return mars_dict
