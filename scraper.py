import requests
import re  # Regex
from bs4 import BeautifulSoup


def extract_url(url):

    if url.find("www.amazon.com") != -1:
        index = url.find("/dp/")
        if index != -1:
            index2 = index + 14
            url = "https://www.amazon.com" + url[index:index2]
        else:
            index = url.find("/gp/")
            if index != -1:
                index2 = index + 22
                url = "https://www.amazon.com" + url[index:index2]
            else:
                url = None
    else:
        url = None
    return url  # https://www.amazon.com/dp/B07K1MDMF3


def get_converted_price(price):
    # Thanks to https://medium.com/@oorjahalt
    converted_price = float(re.sub(r"[^\d.]", "", price))
    return converted_price


def get_product_details(url):
    # User Agent (Just google it)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 OPR/64.0.3417.92"}
    # dictionary product details
    details = {
        "name": "", "price": 0, "deal": True, "url": ""}
    # use extract url function
    _url = extract_url(url)

    if _url == "":  # if url empty
        details = None  # zonk
    else:
        page = requests.get(url, headers=headers)  # request
        soup = BeautifulSoup(page.content, "html5lib")  # html
        title = soup.find(id="productTitle")  # tittle element
        price = soup.find(id="priceblock_dealprice")  # deal price element
        if price is None:  # if no deal price
            # change price to normal price
            price = soup.find(id="priceblock_ourprice")
            # set deal in dictionary to false
            details["deal"] = False
        if title is not None and price is not None:  # tittle and price not empty
            # strip() function remove any trailing and leading spaces and set the return in dictionary
            details["name"] = title.get_text().strip()
            # use convert price function and set the return in dictionary
            details["price"] = get_converted_price(price.get_text())
            # set value on dictionary
            details["url"] = _url
        else:
            return None
    return details  # this fucntion return the dictionary


# print(get_product_details("https://www.amazon.com/XPG-SX8200-Gen3x4-3000MB-ASX8200PNP-512GT-C/dp/B07K1MDMF3/ref=sr_1_3?crid=39D7MWMXC7XAM&keywords=adata%2Bxpg%2Bsx8200%2Bpro%2Bnvme%2Bpcie%2Bm.2%2B256gb&qid=1573386028&sprefix=ADATA%2BXPG%2BSX8200%2Bpro%2B256%2Caps%2C400&sr=8-3&th=1"))

print(get_product_details(
    "https://www.amazon.com/dp/B07K1J3C23/ref=twister_B07WQKKS8V?_encoding=UTF8&psc=1"))
