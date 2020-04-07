#!/usr/bin/python
# Copyright 2020 Laurent Domb
#
# File: create_asana_task.py 
#
# Asana scripts is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Asana is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Asana scripts.  If not, see <http://www.gnu.org/licenses/>.


import os
import json
import requests
import pyfiglet
from dotenv import load_dotenv
load_dotenv()

### Load token and workspace 
auth_token = os.getenv('AUTH_TOKEN')
#workspace = os.getenv('WORKSPACE')
projectid = os.getenv('PROJECTID')
#path = os.getenv('PATHTOFILE')

ascii_banner = pyfiglet.figlet_format("Asana Task")
print(ascii_banner)

auth_token = os.getenv('AUTH_TOKEN')
hed = {'Authorization': 'Bearer ' + auth_token}

url = 'https://app.asana.com/api/1.0/workspaces'
response = requests.get(url,headers=hed)

dict = json.loads(response.text)

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
        "assignee": assignee}}

#url = 'https://app.asana.com/api/1.0/tasks'
url = 'https://app.asana.com/api/1.0/tasks?projects='+projectid+'&workspace='+workspace

response = requests.post(url, json=data, headers=hed)

#print(response)
#print(response.json())
