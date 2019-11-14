
def extract_url(url):

    if url.find("www.amazon.com") != -1:
        index = url.find("/dp/")
        if index != -1:
            index2 = index + 14
            url = "https://www.amazon.com" + url[index:index2]
            trim1 = url[index:index2]
            # """
        else:
            index = url.find("/gp/")
            if index != -1:
                index2 = index + 22
                url = "https://www.amazon.com" + url[index:index2]
                # trim1 = url[index:index2]
            else:
                url = None
                # """
    else:
        url = None
    return url, index, index2, trim1


print(extract_url(
    "https://www.amazon.com/dp/B07K1J3C23/ref=twister_B07WQKKS8V?_encoding=UTF8&psc=1"))

print(extract_url(
    "https://www.amazon.com/XPG-SX8200-Gen3x4-3000MB-ASX8200PNP-512GT-C/dp/B07K1MDMF3"))
