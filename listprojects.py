#!/usr/bin/python

import os
import json
import requests
from dotenv import load_dotenv
load_dotenv()

### Load token
auth_token = os.getenv('AUTH_TOKEN')
hed = {'Authorization': 'Bearer ' + auth_token}

### Load workspace
url = 'https://app.asana.com/api/1.0/workspaces'
response = requests.get(url,headers=hed)

dict = json.loads(response.text)

print("This is your workspace")
print(dict['data'][0]['gid'])
workspace=dict['data'][0]['gid']

### Load Teams
url = 'https://app.asana.com/api/1.0/users/me/teams?organization='+workspace
response = requests.get(url,headers=hed)
dict = json.loads(response.text)
teams = dict['data']

### Load Projects & Print
for t in teams:
    print('Team: '+ t['name'])
    param = {'team': t['gid']}
    
    url = 'https://app.asana.com/api/1.0/projects?limit=5&opt_fields=id,owner.name,name,workspace.id,workspace.name&workspace='+workspace
    response = requests.get(url,headers=hed,params=param)

    dict = json.loads(response.text)
    dict_nice = json.dumps(dict['data'], indent=2)
    print(dict_nice)

    while 'uri' in dict:
        uri=dict['next_page']['uri']
        response = requests.get(uri,headers=hed,params=param)
        dict = json.loads(response.text)
        if 'data' in dict:
            dict_nice = json.dumps(dict['data'], indent=2)
            print(dict_nice)
        else:
            break
        if 'uri' not in dict:
            break