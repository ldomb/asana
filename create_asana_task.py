#!/usr/bin/python

import os
import json
import requests
import pyfiglet
from dotenv import load_dotenv
load_dotenv()

### Load token and workspace 
auth_token = os.getenv('AUTH_TOKEN')
#workspace = os.getenv('WORKSPACE')
path = os.getenv('PATHTOFILE')

ascii_banner = pyfiglet.figlet_format("Asana Task")
print(ascii_banner)

auth_token = os.getenv('AUTH_TOKEN')
hed = {'Authorization': 'Bearer ' + auth_token}

url = 'https://app.asana.com/api/1.0/workspaces'
response = requests.get(url,headers=hed)

dict = json.loads(response.text)

print("This is your workspace")
workspace=(dict['data'][0]['gid'])

### input needed 
taskname = raw_input("Enter task name : ")
due_on = raw_input("Enter due on date 2020-04-20: ")
assignee = raw_input("Enter the assignee's email: ")
notes = raw_input("Enter your description: ")

#filename = raw_input("Enter the filename from your message : ")
#pathtofile = path+filename

## open meeting file with task info
#with open(pathtofile, 'r') as file:
#    notes = file.read().replace('\n', '')

hed = {'Authorization': 'Bearer ' + auth_token}
data = {"data": {"name": taskname, 
        "completed": "false",
        "due_on": due_on,
        "notes": notes,
        "assignee": assignee,
        "workspace": workspace}}

url = 'https://app.asana.com/api/1.0/tasks'
response = requests.post(url, json=data, headers=hed)

#print(response)
#print(response.json())
