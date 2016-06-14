from bs4 import BeautifulSoup
import requests
import re
import urllib.request as urllib2
import os
import re
import datetime
import random

import groupy
from groupy import Bot
from groupy import attachments
from groupy import User

PATH = "/home/jbuchanan11/code/python/groupmememebot/memes/"

def get_soup(url,header):
  return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)), "lxml")

def pull_images(query):
    image_type = "action"
    # you can change the query for the image  here  
    query= query.split()
    query='+'.join(query)
    url=url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
    print (url)
    header = {'user-agent': 'mozilla/5.0'} 
    soup = get_soup(url,header)

    images = [a['src'] for a in soup.find_all("img", {"src": re.compile("gstatic.com")})]
    
    rand = random.randint(1,20)
    count = 1
    for img in images:
        if (rand == count):
            raw_img = urllib2.urlopen(img).read()

            cntr = len([i for i in os.listdir(PATH) if image_type in i]) + 1
            print (cntr)
            f = open(PATH + image_type + "_"+ str(cntr)+".jpg", 'wb')
            f.write(raw_img)
            f.close()
        count = count + 1

groups = groupy.Group.list()
members = groupy.Member.list()
bots = groupy.Bot.list()
group = groups.first
bot = bots.first
#print("joined " + group)

lastmsg = ""
lasttime = datetime.datetime.now()

while True:
    messages = group.messages()
    message = messages.newest
    print("1")
    for m in messages:
        if (m.name != User.get().name and len(m.likes()) > 2):
            like = True
            for l in m.likes():
                if (str(l) == str(User.get().name)):
                    print(l)
                    like = False
            if (like):
                m.like()
    print("2")

    hours = datetime.datetime.now().time().hour
    if (message != lastmsg):
        lasttime = datetime.datetime.now()
        print(message)
        lastmsg = message
    
    if (message.name != User.get().name):
        m = re.match(r"(.*)?give me a meme about (.*)", str(message), flags=re.I)
        if m:
            pull_images(m.group(2) + " meme")

        filenames = next(os.walk(PATH))[2]
        for f in filenames:
            image_attachment = attachments.Image.file(open(PATH + f, 'rb'))
            bot.post("",image_attachment.url)
            os.remove(PATH + f)
    print(3)


 
        


   

   

    

