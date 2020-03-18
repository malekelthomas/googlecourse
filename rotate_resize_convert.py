#!/usr/bin/env python3

from PIL import Image
import os

path = os.getcwd()
for root, dirs, files in os.walk(path+"/images"):
  for file in files:
    imPath = os.path.join(root, file)
    if imPath.endswith(".DS_Store"):
      continue
    else:
      im = Image.open(imPath)
      im.rotate(90).resize((128,128)).convert("RGB").save("/opt/icons/{}.jpeg".format(file), "jpeg")