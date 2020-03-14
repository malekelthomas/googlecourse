#!/usr/bin/env python3

import operator
import re
import sys
import csv

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
  file.close()

#print(per_user)
sortedperusr = sorted(per_user.items(),key=operator.itemgetter(0))
sortedperusr.insert(0, ("Username", "INFO", "ERROR"))
print(sortedperusr)
#print(errormsgs)
sortederrs = sorted(errormsgs.items(),key=operator.itemgetter(1))
sortederrs.insert(0, ("Error", "Count"))
print(errormsgs)

with open("user_statistics.csv", "w") as f:
  for data in sortedperusr:
    f.write("{}\n".format(data))
  f.close()


with open("error_message.csv", "w") as f:
  for data in sortederrs:
    f.write("{}\n".format(data))
  f.close()