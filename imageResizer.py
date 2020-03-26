#!/usr/bin/env python3

from PIL import Image
import os

path = os.getcwd()
for root, dirs, files in os.walk(path+"/supplier-data/images"):
  for file in files:
    print(file)
    imPath = os.path.join(root, file)
    if file == "LICENSE" or file == "README":
      continue
    else:
      outfile = os.path.splitext(imPath)[0] + ".jpeg"
      im = Image.open(imPath)
      im.resize((600,400)).convert("RGB").save(outfile, "jpeg")