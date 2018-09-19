
# Mission to Mars


```python
# Dependencies and Setup
import pandas as pd
import requests as req
import time
from splinter import Browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
```


```python
# Initialize Chrome browser
chrome_options = Options()
chrome_options.add_argument('--headless') # Runs Chrome in headless mode.
chrome_options.add_argument('--no-sandbox') # # Bypass OS security model
chrome_options.add_argument('start-maximized')
chrome_options.add_argument('disable-infobars')
chrome_options.add_argument('--disable-extensions')
```


```python
executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False, options=chrome_options)
```

## NASA Mars News


```python
url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
```


```python
browser.visit(url)
html_code = browser.html
html_clean = BeautifulSoup(html_code, "html.parser")
```


```python
news_title = html_clean.find('div', class_='content_title').text
news_paragraph = html_clean.find('div', class_='article_teaser_body').text
```


```python
print('Latest News Title\t{}'.format(news_title))
print('Latest Paragraph Text\t{}'.format(news_paragraph))
```

    Latest News Title	MarCO Makes Space for Small Explorers
    Latest Paragraph Text	A pair of NASA CubeSats flying to Mars are opening a new frontier for small spacecraft.


## JPL Mars Space Images - Featured Image


```python
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
```


```python
browser.visit(url)
html_code = browser.html
html_clean = BeautifulSoup(html_code, "html.parser")
```


```python
featured_image_url_a_way = html_clean.find('a', {'id': 'full_image', 'data-fancybox-href': True}).get('data-fancybox-href')
```


```python
featured_image_url_b_way = html_clean.find_all('a', class_='fancybox')[0].get('data-fancybox-href').strip()
```


```python
print('Featured Image URL:\thttps://www.jpl.nasa.gov{}'.format(featured_image_url_a_way))
print('Featured Image URL:\thttps://www.jpl.nasa.gov{}'.format(featured_image_url_b_way))
```

    Image URL:	https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA16028_ip.jpg
    Image URL:	https://www.jpl.nasa.gov/spaceimages/images/mediumsize/PIA16028_ip.jpg


### Mars Weather


```python
url = 'https://twitter.com/marswxreport?lang=en'
```


```python
browser.visit(url)
html_code = browser.html
html_clean = BeautifulSoup(html_code, "html.parser")
```


```python
mars_weather = html_clean.select('#stream-items-id > li p')[0].text
```


```python
print('Mars Weather\t{}'.format(mars_weather))
```

    Mars Weather	Sol 2171 (2018-09-14), high -12C/10F, low -65C/-84F, pressure at 8.79 hPa, daylight 05:43-17:59


### Mars Facts


```python
url = 'https://space-facts.com/mars/'
```


```python
mars_facts = pd.read_html(url)
mars_facts
```




    [                      0                              1
     0  Equatorial Diameter:                       6,792 km
     1       Polar Diameter:                       6,752 km
     2                 Mass:  6.42 x 10^23 kg (10.7% Earth)
     3                Moons:            2 (Phobos & Deimos)
     4       Orbit Distance:       227,943,824 km (1.52 AU)
     5         Orbit Period:           687 days (1.9 years)
     6  Surface Temperature:                  -153 to 20 °C
     7         First Record:              2nd millennium BC
     8          Recorded By:           Egyptian astronomers]




```python
mars_facts_df = pd.DataFrame(mars_facts[0])
mars_facts_df.columns = ['Description', 'Values']
mars_facts_df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Description</th>
      <th>Values</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Equatorial Diameter:</td>
      <td>6,792 km</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Polar Diameter:</td>
      <td>6,752 km</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Mass:</td>
      <td>6.42 x 10^23 kg (10.7% Earth)</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Moons:</td>
      <td>2 (Phobos &amp; Deimos)</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Orbit Distance:</td>
      <td>227,943,824 km (1.52 AU)</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Orbit Period:</td>
      <td>687 days (1.9 years)</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Surface Temperature:</td>
      <td>-153 to 20 °C</td>
    </tr>
    <tr>
      <th>7</th>
      <td>First Record:</td>
      <td>2nd millennium BC</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Recorded By:</td>
      <td>Egyptian astronomers</td>
    </tr>
  </tbody>
</table>
</div>




```python
mars_facts_html = mars_facts_df.to_html(classes='mars-facts')
mars_facts_html = mars_facts_html.replace('\n', '')
mars_facts_html
```




    '<table border="1" class="dataframe mars-facts">  <thead>    <tr style="text-align: right;">      <th></th>      <th>Description</th>      <th>Values</th>    </tr>  </thead>  <tbody>    <tr>      <th>0</th>      <td>Equatorial Diameter:</td>      <td>6,792 km</td>    </tr>    <tr>      <th>1</th>      <td>Polar Diameter:</td>      <td>6,752 km</td>    </tr>    <tr>      <th>2</th>      <td>Mass:</td>      <td>6.42 x 10^23 kg (10.7% Earth)</td>    </tr>    <tr>      <th>3</th>      <td>Moons:</td>      <td>2 (Phobos &amp; Deimos)</td>    </tr>    <tr>      <th>4</th>      <td>Orbit Distance:</td>      <td>227,943,824 km (1.52 AU)</td>    </tr>    <tr>      <th>5</th>      <td>Orbit Period:</td>      <td>687 days (1.9 years)</td>    </tr>    <tr>      <th>6</th>      <td>Surface Temperature:</td>      <td>-153 to 20 °C</td>    </tr>    <tr>      <th>7</th>      <td>First Record:</td>      <td>2nd millennium BC</td>    </tr>    <tr>      <th>8</th>      <td>Recorded By:</td>      <td>Egyptian astronomers</td>    </tr>  </tbody></table>'



### Mars Hemispheres


```python
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
```


```python
browser.visit(url)
html_code = browser.html
html_clean = BeautifulSoup(html_code, "html.parser")
```


```python
images = html_clean.find('div', class_='collapsible results')

hemisphere_image_urls = []
```


```python
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
```


```python
print(hemisphere_image_urls)
```

    [{'title': 'Cerberus Hemisphere Enhanced', 'image_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'}, {'title': 'Schiaparelli Hemisphere Enhanced', 'image_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'}, {'title': 'Syrtis Major Hemisphere Enhanced', 'image_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'}, {'title': 'Valles Marineris Hemisphere Enhanced', 'image_url': 'http://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'}]

