import json
import os
import scrapeHashTag
from urllib.request import Request, urlopen
from instabot import Bot
from loginDetails import instaLoginDetails
from cropImg import cropCatImg

# initialize login information for instagram
initLogin = instaLoginDetails()

# fetch json from catAPI
with urlopen("https://api.thecatapi.com/v1/images/search") as url:
    data = json.loads(url.read())
    catDict = data[0]
    catImgUrl = catDict["url"]+"?api_key="+instaLoginDetails.apiKey

# open the fetched url and save it to a jpg file
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 "
                         "Safari/537.3"}
reg_url = catImgUrl
req = Request(url=reg_url, headers=headers)
html = urlopen(req).read()
f = open('tempCatImg.jpg', 'wb')
f.write(urlopen(req).read())
f.close()

# maintain a file to keep record of the test number (used in caption to distinguish between posts)
f = open("testNum.txt", "r")
lastNum = int(f.read())
lastNum += 1
f.close()

f = open("testNum.txt", "w")
f.write(str(lastNum))
f.close()

cropCatImg()

# create bot, login and upload image
botToPost = Bot()
botToPost.login(username=initLogin.userName, password=initLogin.passWord)

# check for top hashtags
hashTagList = scrapeHashTag.fetchPopularHashTags()

newTestCaption = "test#000"+str(lastNum)+"\n"+str(hashTagList[0])+" "+str(hashTagList[1])+" "+str(hashTagList[2])
botToPost.upload_photo("final.jpg", caption=newTestCaption)

# delete the images so no conflicts arise the next time we run the program
os.remove("tempCatImg.jpg")
os.remove("final.jpg.REMOVE_ME")

