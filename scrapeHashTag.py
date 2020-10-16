# fetch the top instagram hashtags from top-hashtags.com

import requests
from bs4 import BeautifulSoup

def fetchPopularHashTags():
    popularHashTags = []
    fetchUrl = "https://top-hashtags.com/instagram/"
    scrapedPageData = requests.get(fetchUrl)
    dataSoup = BeautifulSoup(scrapedPageData.content, "html.parser")
    grabDiv = dataSoup.find("div", class_="entry-content clear")
    grabDivTag = grabDiv.find_all("div", class_="i-tag")
    for popularHashTag in grabDivTag:
        popularHashTags.append(popularHashTag.a.text)

    return popularHashTags


if __name__ == "__main__":
    print(fetchPopularHashTags())


