#!/usr/bin/env python3

import shutil
import psutil
import emails
import os
import socket 

def systemcheck():
  cpu_usage = psutil.cpu_percent(interval=60)
  disk_usage = psutil.disk_usage("/")
  mem_usage = psutil.virtual_memory()
  host_name = socket.gethostname()
  host_ip = socket.gethostbyname(host_name)

 
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  body = "Please check your system and resolve the issue as soon as possible"
  
  if cpu_usage > 80:
    error_message = "Error - CPU usage is over 80%"
    message = emails.generate_error_report(sender, receiver, error_message, body)
    emails.send_email(message)
  elif mem_usage[1] < 500:
    error_message = "Error - Available memory is less than 500MB"
    message = emails.generate_error_report(sender, receiver, error_message, body)
    emails.send_email(message)
  elif disk_usage[3] > 80:
    error_message = "Error - Available disk space is less than 20%"
    message = emails.generate_error_report(sender, receiver, error_message, body)
    emails.send_email(message)
  elif host_ip != "127.0.0.1":
    error_message = "Error - localhost cannot be resolved to 127.0.0.1"
    message = emails.generate_error_report(sender, receiver, error_message, body)
    emails.send_email(message)

def main():
  systemcheck()

if __name__ == "__main__":
  main()
