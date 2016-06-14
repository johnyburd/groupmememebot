from bs4 import BeautifulSoup
import requests
import re
import urllib.request as urllib2
import os
import re
#import datetime
import random
import time

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
#Bot.create("twinkle_toes97", group, "https://i.groupme.com/1125x1500.jpeg.7e3ad500b839434c9eb42494790a9f10")
#print("joined " + group)

lastmsg = group.messages().newest
lasttime = time.time()

while True:
    messages = group.messages()
    message = messages.newest
    del messages[15:]
    for m in messages:
        if (str(m.name) != str(User.get().name) and len(m.likes()) > 2 and str(m.name) != "twinkle_toes97"):
            like = True
            for l in m.likes():
                if (str(l) == str(User.get().name)):
                    like = False
            if (like):
                m.like()

    if (str(message) != str(lastmsg)):
        #lasttime = datetime.datetime.now()
        lasttime = int(time.time())
        print(message)
        lastmsg = message
    now = int(time.time())
    d = divmod(now - lasttime,86400)  # daystt
    h = divmod(d[1],3600)  # hours
    m = divmod(h[1],60)  # minutes
    s = m[1]  # seconds
    print ('%d days, %d hours, %d minutes, %d seconds' % (d[0],h[0],m[0],s))

    if (d[0] < 1 and h[0] < 1 and m[0] > 2 and m[0] < 10):
        if (random.randint(0,80000) == 0):
            pull_images("dank meme")





    if (message.name != User.get().name):
        m = re.match(r"(.*)meme(s)? .*about (.*)", str(message), flags=re.I)
        if m:
            pull_images(m.group(3) + " meme")
            print("found: " + m.group(3))

    filenames = next(os.walk(PATH))[2]
    for f in filenames:
        image_attachment = attachments.Image.file(open(PATH + f, 'rb'))
        bot.post("",image_attachment.url)
        os.remove(PATH + f)



