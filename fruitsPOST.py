#!/usr/bin/env python3

import os
import requests

fruits = {}
path = os.getcwd()
for root, dirs, files in os.walk(path+"/supplier-data/descriptions"):
  for file in files:
    fpath = os.path.join(root,file)
   with open(fpath, "r") as f:
      newFruit = {}
      newFruit["name"] = f.readline()
      newFruit["weight"] = int(f.readline().strip(" lbs\n"))
      newFruit["description"] = f.readlines()
      if len(newFruit["description"]) > 1:
        newFruit["description"] = newFruit["description"][0]
      filenameNoExt = f.name.split("/")[5].strip(".txt")
      img = filenameNoExt+".jpeg"
      newFruit["image_name"] = img
      fruits[newFruit["name"]] = newFruit
      #response = requests.post("http://35.224.157.53/fruits/", data=newFruit)
      #print(response.text)

for key, item in zip(fruits.keys(),fruits.items()):
  url = "http://localhost/fruits/"
  response = requests.post(url, data=item[1])
  print(response.text)
