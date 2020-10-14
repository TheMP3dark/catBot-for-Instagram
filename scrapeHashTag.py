# fetch the top instagram hashtags from top-hashtags.com

import requests
from bs4 import BeautifulSoup

def fetchPopularHashTags():
    fetchUrl = "https://top-hashtags.com/instagram/"
    scrapedPageData = requests.get(fetchUrl)
    dataSoup = BeautifulSoup(scrapedPageData.content, "html.parser")
    grabDiv = dataSoup.find("div", class_="entry-content clear")
    grabDivTag = str(grabDiv.find_all("div", class_="i-tag"))
    hashListParent = grabDivTag.split("#")
    hashList = hashListParent[1::1]

    popularHashTags = []
    for items in hashList:
        hashes = items.split("</a>")
        popularHashTags.append(hashes[0])

    return popularHashTags


if __name__ == "__main__":
    print(fetchPopularHashTags())


