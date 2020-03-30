#!/usr/bin/python

from json2html import *
import os
import json
import requests
from dotenv import load_dotenv
load_dotenv()

### Load token and workspace 

auth_token = os.getenv('AUTH_TOKEN')
mytasklist = os.getenv('MYTASKLIST')
project = os.getenv('PROJECTID')
hed = {'Authorization': 'Bearer ' + auth_token}

url = 'https://app.asana.com/api/1.0/user_task_lists/'+mytasklist+'/tasks?opt_fields=due_on,notes,name'
response = requests.get(url,headers=hed)
dict = json.loads(response.text)
dict_nice = json.dumps(dict, indent=2)
print(dict_nice)
#tasklist=json2html.convert(json = dict_nice)
#print(tasklist)
