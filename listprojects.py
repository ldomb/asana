#!/usr/bin/python
# Copyright 2020 Laurent Domb
#
# File: listprojects.py
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
