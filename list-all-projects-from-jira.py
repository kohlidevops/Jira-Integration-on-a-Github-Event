# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://slakshminarayanan.atlassian.net/rest/api/3/project"

API_TOKEN = "your-jira-api-token-here"
auth = HTTPBasicAuth("slakshminarayanan.6fs@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

#print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
output = json.loads(response.text)
name = output[1]["name"]
print(name)
