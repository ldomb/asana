#!/usr/bin/python

import os
import requests
import pyfiglet
from dotenv import load_dotenv
load_dotenv()

### Load token and workspace 
auth_token = os.getenv('AUTH_TOKEN')

auth_token = os.getenv('AUTH_TOKEN')
hed = {'Authorization': 'Bearer ' + auth_token}

url = 'https://app.asana.com/api/1.0/workspaces'
response = requests.get(url,headers=hed)

print(response.json())
