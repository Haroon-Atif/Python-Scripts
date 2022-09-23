#!/usr/bin/env python3

from PIL import Image
import os
#set paths
input_path = os.path.expanduser('~') + '<path>'
output_path = os.path.expanduser('~') + '<path>'
#iterate over each item in directory 
for image in os.listdir(input_path):
  #only get .jpeg files and dont get hidden files
  if '.' not in image[0] and '.tiff' in image:
    with Image.open(input_path+image) as im:
      #change to preferred format and save to output path
      im.resize((600,400)).convert("RGB").save(output_path + image.split(".")[0] + ".jpeg", 'JPEG')
