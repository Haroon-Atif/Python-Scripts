#!/usr/bin/env python3
import os
import reports
from datetime import date
import emails

input_path = os.path.expanduser('~') + '<path>'
#function that processes data and turns it into a list of strings 
def process():
  data_list = []
  modify = []
  final = []
  items = os.listdir(input_path)
  os.chdir(input_path)
  for item in items:
    with open(item, 'r') as f:
      name = f.readline().rstrip('\n')
      weight = f.readline().rstrip('\n')
      description = f.readline().rstrip('\n')
    comment = {"name": name, "weight": weight}
    data_list.append(comment)
    for i in data_list:
      for k, v in i.items():
        modify.append(k+': '+v)
        split = "<br/>".join(modify)
    data_list = []
    modify = []
    final.append(split+"<br/>")
  return final
#email sending and generating func
def send_email():
  sender = "automation@example.com"
  recipient = "user@example.com"
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attatched to this email."
  msg = emails.generate(sender, recipient, subject, body, '/tmp/processed.pdf')
  emails.send(msg)
def send_report():
  #setting the date
  today = date.today()
  date = today.strftime("%B %d, %Y")
  #setting the title
  title = "Processed Update on {}".format(date)
  #setting the paragraph in proper format
  summary = process()
  paragraph = '<br/>'.join(summary)
  #generating report
  reports.generate('/tmp/processed.pdf', title, paragraph)
if __name__ == "__main__":
  send_report()
  send_email()
  
