#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd
import json
import numpy as np
import re

from sqlalchemy import create_engine
import psycopg2

# from config import db_password
# from config import db_password

import time


# In[2]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[3]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[ ]:





# In[4]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[5]:


# assign the title and summary text to variables
# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[6]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# In[7]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[8]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[9]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[10]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[11]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# In[12]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[13]:


# The Module 10 Challenge Deliverable
# Visit the NASA Mars News Site


# In[14]:


# Visit the mars nasa news site
url = 'https://data-class-mars.s3.amazonaws.com/Mars/index.html'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[15]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[16]:


slide_elem.find('div', class_='content_title')


# In[17]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[18]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# In[19]:


# JPL Space Images Featured Image


# In[20]:


# Visit URL
url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
browser.visit(url)


# In[21]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[22]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[23]:


# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[24]:


# Use the base url to create an absolute url
img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'
img_url


# In[25]:


# Mars Facts


# In[26]:


df = pd.read_html('https://data-class-mars-facts.s3.amazonaws.com/Mars_Facts/index.html')[0]
df.head()


# In[27]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[28]:


df.to_html()


# In[29]:


# D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles
# Hemispheres


# In[30]:


# 1. Use browser to visit the URL 
url = 'https://data-class-mars-hemispheres.s3.amazonaws.com/Mars_Hemispheres/index.html'

browser.visit(url)


# In[32]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
links_hemisphere=browser.find_by_css("a.product-item img")
for item in range(len(links_hemisphere)):
    hemi={}
 # We have to find the elements on each loop to avoid a stale element exception
    browser.find_by_css('a.product-item img')[item].click()
    # Next, we find the Sample image anchor tag and extract the href
    sample_elem = browser.links_hemisphere.find_by_text('Sample').first
    hemi['img_url'] = sample_elem['href']
    # Get Hemisphere title
    hemi['title'] = browser.find_by_css('h2.title').text
    # Append hemisphere object to list
    hemisphere_image_urls.append(hemi)
    # Finally, we navigate backwards
    browser.back()
    


# In[33]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[34]:


# 5. Quit the browser
browser.quit()


# In[ ]:




