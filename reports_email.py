#!/usr/bin/env python3

import os
import datetime
import reports
import emails


def fruitSummary():
  path = os.getcwd()
  summary = []
  for root, dirs, files in os.walk(path+"/supplier-data/descriptions"):
    for file in files:
      fpath = os.path.join(root,file)
      with open(fpath, "r") as f:
        summary.append("name: {}".format(f.readline()))
        summary.append("weight: {}\n".format(f.readline()))
        f.close()
  return summary

def main():
  summary = fruitSummary()
  summary ="<br/>".join(summary)
  report_title = "Processed Update on {} {}, {}".format(datetime.datetime.now().now().strftime("%B"), datetime.date.today().day, datetime.date.today().year)
  print(report_title)
  attachment = "/tmp/processed.pdf"
  reports.generate_report(attachment, report_title, summary)
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  subject = "Upload Completed - Online Fruit Store"
  message = emails.generate_email(sender, receiver, subject, body, attachment)
  emails.send_email(message)

if __name__ == "__main__":
  main()
