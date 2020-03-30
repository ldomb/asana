#!/usr/bin/python

import os
import json
import requests
from dotenv import load_dotenv
load_dotenv()

### Load token and workspace 
auth_token = os.getenv('AUTH_TOKEN')
hed = {'Authorization': 'Bearer ' + auth_token}

url = 'https://app.asana.com/api/1.0/workspaces'
response = requests.get(url,headers=hed)

dict = json.loads(response.text)

print("This is your workspace")
print(dict['data'][0]['gid'])
workspace=dict['data'][0]['gid']

url = 'https://app.asana.com/api/1.0/projects?limit=5&opt_fields=id,owner.name,name,workspace.id,workspace.name&workspace='+workspace


response = requests.get(url,headers=hed)

dict = json.loads(response.text)
dict_nice = json.dumps(dict, indent=2)
uri=dict['next_page']['uri']

while dict['next_page']['uri']:
    print(dict_nice)
    response = requests.get(uri,headers=hed)
    dict = json.loads(response.text)
    dict_nice = json.dumps(dict, indent=2)
    uri=dict['next_page']['uri']
