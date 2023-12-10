#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from dataclasses import dataclass, asdict
import json

@dataclass
class Caterory:
   id: str
   name: str

@dataclass
class Page:
   url: str
   name: str

def start_browser():
   options = Options()
   options.add_argument("window-size=1920,1080")
   options.add_argument("--headless")
   driver = webdriver.Chrome(options=options)
   driver.implicitly_wait(2)
   return driver

def main():
   driver = start_browser()
   driver.get("https://www.here.com/docs/bundle/places-search-api-developer-guide/page/topics/place_categories/places-category-system.html")
   pages = collect_pages(driver)
   print_categoties(pages, driver)

   
def collect_pages(driver):
   nav_links = driver.find_elements(By.XPATH, '//ul[@id="placessearchapideveloperguide-PlacesCategorySystem"]//li/div/span/a')
   pages = []
   for e in nav_links:
      page = Page(e.get_attribute("href"), e.text) 
      pages.append(page)
       
   assert len(pages) == 11
   return pages


def print_categoties(pages, driver):
   for page in pages:
      data = extract_category(page.url, driver)  
      s_arr = page.name.split('-', 1)
      nav_category = Caterory(s_arr[0].strip(), s_arr[1].strip())
      print(json.dumps(asdict(nav_category)))
      for category in data:
         print(json.dumps(asdict(category)))
      
def extract_category(link, driver):
   driver.get(link)
   tables = driver.find_elements(By.XPATH, '//table')
   data = []
   for table in tables:
      rows = table.find_elements(By.TAG_NAME, "tr")
      for row in rows:  
         col = row.find_elements(By.TAG_NAME, "td")
         res = []
         for el in col:
            res.append(el.text)
         if len(res) > 0:
            category = Caterory(res[0], res[1])     
            data.append(category)
   return data

if __name__ == "__main__":
   main()

   
