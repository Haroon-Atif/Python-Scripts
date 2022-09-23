#!/usr/bin/env python3
import shutil
import psutil
import emails
import socket

#set constants
body = "Please check your system and resolve the issue as soon as possible"
sender = "automation@example.com"
recipient = "user@example.com"

#cpu check function to make sure we arent using too much
def cpu_check():
  cpu_percentage = psutil.cpu_percent(1)
  if (cpu_percentage > 80):
    msg = "Error - CPU usage is over 80%"
    return msg
#memory check warning
def memory_check():
  memory = psutil.virtual_memory()
  threshold = 500*1024*1024
  if (memory.available <= threshold):
    msg = "Error - Available memory is less than 500MB"
    return msg
# disk check function
def disk_check():
  disk_total, disk_used, disk_free = shutil.disk_usage("<path>")
  disk_percent = (disk_free/disk_total)*100
  if (disk_percent < 20):
    msg = "Error - Available disk space is less than 20%"
    return msg

def localhost_check():
  domain_resolve = socket.gethostbyname('localhost')
  if (domain_resolve != '127.0.0.1'):
    msg = "Error - localhost cannot be resolved to 127.0.0.1"
    return msg


if __name__ == "__main__":
#only send email if there is an error

  disk_msg = disk_check()
  if disk_msg != None:
    email = emails.generate(sender, recipient, disk_msg, body, 'nopath')
    emails.send(email)
  host_msg = localhost_check()
  if host_msg != None:
    email = emails.generate(sender, recipient, host_msg, body, 'nopath')
    emails.send(email)
  cpu_msg = cpu_check()
  if cpu_msg != None:
    email = emails.generate(sender, recipient, cpu_msg, body, 'nopath')
    emails.send(email)
  mem_msg = memory_check()
  if mem_msg != None:
    email = emails.generate(sender, recipient, mem_msg, body, 'nopath')
    emails.send(email)
