import urllib.request
import urllib.error
import re
from bs4 import BeautifulSoup

def main():
  brand_id = 19077
  brand_id = 19016
  cap_brand_id = brand_id + 100

  while brand_id < cap_brand_id:
    brand_name = get_brand_name_by_brand_id(brand_id)
    turnover = get_turnover_by_brand_id(brand_id)
    print(str(brand_id) + ": " + brand_name)
    brand_id += 1

def get_brand_name_by_brand_id(brand_id):
  intr_url_pattern = "http://mall.360buy.com/introduction-[BRAND_ID].html"
  current_intr_url = intr_url_pattern.replace("[BRAND_ID]",str(brand_id))
  res = get_content_by_url(current_intr_url)
  if res is None:
    return ""
  brand_name = get_brand_name_from_brand_intr_page(res)
  return brand_name or ""

def get_brand_name_from_brand_intr_page(intr_page_html):
  index_href_pattern = re.compile("com/index")
  soup = BeautifulSoup(intr_page_html)
  index_a = soup.find("a", href=index_href_pattern)
  index_a_soup = BeautifulSoup(str(index_a))
  return index_a_soup.text

def get_turnover_by_brand_id(brand_id):
  goods_list_url_pattern = "http://mall.360buy.com/shopWare-[BRAND_ID]-0-0-[PAGE_NUMBER]-.html"
  page_number = 1
  current_goods_list_page = goods_list_url_pattern.replace("[BRAND_ID]", str(brand_id)).replace("[PAGE_NUMBER]", str(page_number))
  goods_list = get_goods_list_from_goods_list_page(current_goods_list_page)
  return goods_list

def get_goods_list_from_goods_list_page(goods_list_page_url):
  goods_list_page_html = get_content_by_url(goods_list_page_url)
  if goods_list_page_html is None:
    return {}
  soup = BeautifulSoup(goods_list_page_html)
  goods_div = soup.find("div", class_="")

def get_content_by_url(url):
  try:
    req = urllib.request.urlopen(url)
    res = req.read()
    return res
  except urllib.error.HTTPError as e:
    print("URL Error")
    return None

if __name__ == "__main__":
  main()
