
#!/usr/bin/env python3

import os
import requests


path = os.getcwd()
for root, dirs, files in os.walk(path+"/supplier-data/images"):
  for file in files:
    fpath = os.path.join(root,file)
    if file == "LICENSE" or file == "README":
      continue
    url = "http://localhost/upload/"
    with open(fpath, 'rb') as opened:
      r = requests.post(url, files={'file':opened})
      print(r.text)