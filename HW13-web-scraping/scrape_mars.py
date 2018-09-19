#!/opt/anaconda3/bin/python
# coding: utf-8

'''
###################################################################################
# @script scrape_mars.py                                                          #
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
import time
from splinter import Browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# Initialize Chrome browser
chrome_options = Options()
chrome_options.add_argument('--headless') # Runs Chrome in headless mode.
chrome_options.add_argument('--no-sandbox') # # Bypass OS security model
chrome_options.add_argument('start-maximized')
chrome_options.add_argument('disable-infobars')
chrome_options.add_argument('--disable-extensions')

executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False, options=chrome_options)

'''
## Functions
-------------------------------------------------
'''
def browser_soup(url):
	browser.visit(url)
	code = browser.html
	html = BeautifulSoup(code, "html.parser")
	return html

def mars_news():
	url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
	html_clean = browser_soup(url)
	
	news_title = html_clean.find('div', class_='content_title').text
	news_paragraph = html_clean.find('div', class_='article_teaser_body').text

	return news_title, news_paragraph 

def mars_featured_image():
	url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
	html_clean = browser_soup(url)

	featured_image_url = html_clean.find('a', {'id': 'full_image', 'data-fancybox-href': True}).get('data-fancybox-href')

	return featured_image_url

def mars_weather():
	url = 'https://twitter.com/marswxreport?lang=en'
	html_clean = browser_soup(url)

	mars_weather = html_clean.select('#stream-items-id > li p')[0].text

	return mars_weather

def mars_facts
	url = 'https://space-facts.com/mars/'
	mars_facts = pd.read_html(url)

	mars_facts_df = pd.DataFrame(mars_facts[0])
	mars_facts_df.columns = ['Description', 'Values']

	mars_facts_html = mars_facts_df.to_html(classes='mars-facts')
	mars_facts_html = mars_facts_html.replace('\n', '')

	return mars_facts_html

def mars_hemisphere_images():
	url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

	browser.visit(url)
	html_code = browser.html
	html_clean = BeautifulSoup(html_code, "html.parser")

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

	return hemisphere_image_urls

