#from groupy import Bot, Group

#group = Group.list().first
#bot = Bot.create('R2D2', group)
#bot.post("test post from a robo")

from bs4 import BeautifulSoup
import requests
import re
import urllib.request as urllib2
import os
import groupy
from PIL import Image
from groupy import Bot
from groupy import attachments
from groupy import User
def get_soup(url,header):
  return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)), "lxml")

image_type = "Action"
# you can change the query for the image  here  
query = "dank memes"
query= query.split()
query='+'.join(query)
url=url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
print (url)
header = {'User-Agent': 'Mozilla/5.0'} 
soup = get_soup(url,header)

images = [a['src'] for a in soup.find_all("img", {"src": re.compile("gstatic.com")})]
#print images
for img in images:

  raw_img = urllib2.urlopen(img).read()

  #add the directory for your image here 
  DIR="/home/jbuchanan11/"
  cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
  print (cntr)
  f = open(DIR + image_type + "_"+ str(cntr)+".jpg", 'wb')
  f.write(raw_img)
  
  #imgSize = (30,30)

  #img = Image.fromstring('RGBA', imgSize, raw_img)
  #img.save('/home/jbuchanan11/test.png')
  f.close()

groups = groupy.Group.list()
members = groupy.Member.list()
bots = groupy.Bot.list()
group = groups.first
print(groups)
print(members)
print(bots)
print(group.messages())

#group.post("ur mom sux")

'''
last = ""
while True:
    messages = group.messages()
    for m in messages:
        if (len(m.likes()) > 0):
            m.like()
    message = messages.newest
    if (last != message.text):
        print(message.text)
    last = message.text
'''
messages = group.messages()
print(User.get().name)
#for m in messages:
#    m.unlike()


#bot = Bot.list().first

#bot = Bot.create('twinkle_toes97', group)#, "https://i.groupme.com/1125x1500.jpeg.7e3ad500b839434c9eb42494790a9f10")
#filenames = next(os.walk("/home/jbuchanan11/"))[2]

#for f in filenames:
 #   image_attachment = attachments.Image.file(open("/home/jbuchanan11/"+f, 'rb'))
 #   bot.post("",image_attachment.url)


#bot.post("","https://i.groupme.com/1125x1500.jpeg.7e3ad500b839434c9eb42494790a9f10")
#bot.destroy()
#bot.post("this is a test")

   #61350
   #26860


