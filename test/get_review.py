import requests
import time
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import urllib.error
import urllib.request
# import lxml.html
# import selenium.webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# import chromedriver_binary
# from selenium import webdriver

def Image_download(url, nomber):
  dst_path = "images/"+ str(nomber)
  try:
    with urllib.request.urlopen(url) as web_file:
      data = web_file.read()
      with open(dst_path, mode='wb') as local_file:
          local_file.write(data)
  except urllib.error.URLError as e:
    print(e)
    pass




image_url = []
i = 1

# driver = webdriver.Chrome()
url = "https://www.amazon.co.jp/%E6%AD%AF%E8%BB%8A%E3%83%91%E3%83%BC%E3%83%84-500g-%E7%B4%84360%E5%80%8B%E3%82%BB%E3%83%83%E3%83%88-%E3%82%AF%E3%83%A9%E3%83%95%E3%83%88-%E3%83%81%E3%83%A3%E3%83%BC%E3%83%A0/dp/B079DJ8NS6/ref=sr_1_3?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=P1UICUPIZHYZ&keywords=%E9%83%A8%E5%93%81&qid=1582508388&sprefix=%E9%83%A8%E5%93%81%2Caps%2C1245&sr=8-3"
# driver = selenium.webdriver.PhantomJS()
# driver.get(url)

# time.sleep(1)
# graph = driver.find_element_by_class_name("a-spacing-small")
# print(graph)
# actions = ActionChains(driver)
# actions.move_to_element(graph).perform()
# # actions.move_to_element(
# #     driver.find_element_by_class_name("a-spacing-small")
# # ).perform()
# # driver.find_element_by_class_name("imageThumbnail").click()
# # driver.find_element_by_class_name("a-list-item").click()
# driver.find_element_by_class_name("a-button-inner").click()
# time.sleep(5)
# r = driver.page_source.encode('utf-8')
# r = driver.page_source
# image_boxs = driver.find_element_by_class_name("imgTagWrapper")
# driver.save_screenshot("ss.png")

session = HTMLSession()
r = session.get(url)
d_soup = BeautifulSoup(r.content, "html.parser")
review_boxs = d_soup.select(".a-row.a-size-small", recursive=False)
# print(image_boxs)
# print(len(image_boxs))
# driver.close()
for review_box in review_boxs:
  reviews = d_soup.select(".a-icon-alt", recursive=False)
  for review in reviews:
    print(review.get_text())
  # print(image_box)
  # print(image_box.find("img").get("src"))
    time.sleep(0.5)


