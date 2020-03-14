#!/usr/bin/env python3

import operator
import re
import sys

errormsgs = {}
per_user = {}

with open(sys.argv[1], "r") as file:
  for line in file.readlines():
    if re.search(r"ticky: INFO ([\w ]*) ", line):
      usrname = re.search(r'\(([\w.]*)\)', line)
      if usrname != None:
        if usrname.group(1) not in per_user.keys():
          per_user[usrname.group(1)]=[1,0]
        else:
          per_user[usrname.group(1)][0]+=1
    if re.search(r"ticky: ERROR ([\w ]*) ", line):
      usrname = re.search(r'\(([\w.]*)\)', line)
      if usrname != None:
        if usrname.group(1) not in per_user.keys():
          per_user[usrname.group(1)]=[0,1]
        else:
          per_user[usrname.group(1)][1]+=1
      error = re.search(r"ticky: ERROR ([\w ']*) ", line)
      #print(line, error.group(1))
      if error.group(1) not in errormsgs.keys():
        errormsgs[error.group(1)]=1
      else:
        errormsgs[error.group(1)]+=1

#print(per_user)
sortedperusr = sorted(per_user.items(),key=operator.itemgetter(0))
print(sortedperusr)
#print(errormsgs)
sortederrs = sorted(errormsgs.items(),key=operator.itemgetter(1))
print(errormsgs)
