#! /usr/bin/env python3

import os
import requests

#set paths
img_path = os.path.expanduser('~') + '<path>'
descr_path = os.path.expanduser('~') + '<path>'
items = os.listdir(descr_path)
image_items = os.listdir(img_path)

#set iterator and sort list for data processing
i=0
image_items.sort()

#change to directory of objects that need to be written and saved 
os.chdir(descr_path)
#for each file perform an action
for item in items:
  #open each file and read the data into variables
  with open(item, 'r') as f:
    name = f.readline().rstrip('\n')
    weight = f.readline().rstrip('\n')
    int_weight = int(weight.split().pop(0))
    description = f.readline().rstrip('\n')
  #get the name of .jpeg files from images directory 
  image_name = image_items[i]
  #bump iterator by 2 every loop, this is for data processing reasons
  #TODO: make a better version of this
  i+=2
  #create JSON object 
  comment = {"name": name, "weight": int_weight, "description": description, "image_name": image_name}
  #create POST request and upload to website 
  response = requests.post("http://url/", data=comment)
