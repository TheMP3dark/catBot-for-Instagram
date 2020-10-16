pls read dis i spent a lot of time typing it all and even had to watch a video to understand github :(_
<br>
#####UPDATE: Added capability to fetch and add popular hashtags to the title automatically! 
# catBot for Instagram

The aim of this python program is to fetch random cat images using the [catAPI](https://thecatapi.com/) and post them to Instagram using the [instabot library](https://pypi.org/project/instabot/). The program requires you to have an Instagram account beforehand. You will also require an API key for catAPI that you can simply receive in an email after signing up for free [here](https://thecatapi.com/).

# Prerequisites
You will need python to be installed on your machine in order to run the python program. You will also need to install some libraries used by the program manually using pip. 
Run the following command to install the libraries:
<br>
<br>
_**Instabot:**_
<br>
`pip install instabot`
<br>
_**Requests:**_
<br>
`pip install requests`
<br>
_**BeautifulSoup4:**_
<br>
`pip install bs4`

**!!! IMPORTANT !!!**
Before you can run the program, you will need to edit loginDetails.py

    def __init__(self):  
      self.userName = "USER_NAME"  
      self.passWord = "PASSWORD"  
      self.apiKey = "API_KEY"
Replace USER_NAME with your Instagram username (not email id) and PASSWORD with your password. You will also need to replace API_KEY with the api ey you recieve from catAPI as an email.

When you are done with the previous steps, you can run main.py in python using the following command:
<<<<<<< HEAD
<br>
`python main.py`
<br>
=======
`pyt hon main.py`
>>>>>>> f36d78df1a0b2974240519f899b099e84fffedec
Check your Instagram account from a web browser to check if the image has been posted.
    

# Files


1. main.<span></span>py 
2. loginDetails.<span></span>py
3. cropImg.<span></span>py 
4. testNum.txt



## main.<span></span>py

This is the main file that you will need to execute in order to publish a post. Run it using the command: 
`python main.py`

You can give your post a custom caption by replacing newTestCaption with your caption in the following code:

    # create bot, login and upload image
    botToPost = Bot()  
    botToPost.login(username=initLogin.userName, password=initLogin.passWord)  
    newTestCaption = "test#000"+str(lastNum)  
    botToPost.upload_photo("final.jpg", caption=newTestCaption)
 So a custom caption would look something like this:

     # create bot, login and upload image
        botToPost = Bot()  
        botToPost.login(username=initLogin.userName, password=initLogin.passWord)  
        newTestCaption = "test#000"+str(lastNum)  
        botToPost.upload_photo("final.jpg", caption="THIS IS A CUSTOM CAPTION MEOW")

## loginDetails.<span></span>py

This is where your account details and the API key is stored. Before you can run the program, you will need to edit this file.

    def __init__(self):  
      self.userName = "USER_NAME"  
      self.passWord = "PASSWORD"  
      self.apiKey = "API_KEY"
Replace USER_NAME with your Instagram username (not email id) and PASSWORD with your password. You will also need to replace API_KEY with the api ey you recieve from catAPI as an email.

## cropImg.<span></span>py

cropImg.<span></span>py is used to crop the images fetched from the catAPI to a square aspect ratio. This is done as Instagram only allows you to upload images in only some aspect ratios. You can edit this file to get another custom aspect ratio supported by Instagram. The PIL library is used to carry out the cropping task.

## testNum.txt

To keep track of test posts and maintain unique captions for each post, this file is used. It keeps count of the number of times the file is executed. It should contain "0" when you first open the file. It will be incremented by 1 and updated in the text file every time you run the program.

## scrapeHashTag.<span></span>py

This program fetches top hashtags from https://top-hashtags.com/instagram/ and appends it into a list, which is further used to add the custom hashtags to the post caption. We make use of requests library to fetch the page and BeautifulSoup (bs4) for parsing the fetched webpage.
# Future Goals

Some features I am planning to add when I get the time.

~~Automatically add custom #hashtags to make the post more popular
Scrape Instagram for the popular (in this case, cats related) hashtags to give our posts more visibility.~~

## Record the number of likes on posts

catAPI supports sending the number of likes to a fetched image. We can send the number of likes the post gets to catAPI to improve the API.

## Automatic caption through Machine Learning/ Neural Networks

OH LAWD!?!?!
This is my final goal and the main reason for me to make this project.


# THANK THANK

TheMP3dark