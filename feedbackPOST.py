#!/usr/bin/env python3

import os
import requests


files = os.listdir("/data/feedback")

content = {}

for file in files:
  with open("/data/feedback/"+file, "r") as f:
    fileContent = {} 
    fileContent["title"] = f.readline()
    fileContent["name"] = f.readline()
    fileContent["date"] = f.readline()
    fileContent["feedback"] = f.readlines()
    response = requests.post("http://34.70.69.220/feedback/", data=fileContent) #had to append slash to work
    #print(response.text)
    #content[os.path.basename(f.name)] = fileContent #use filenames as keys and fileContent dicts as values

#response = requests.post("http://34.70.69.220/feedback", data=content) #HTTP POST