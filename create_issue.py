# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://slakshminarayanan.atlassian.net/rest/api/3/issue"
API_TOKEN = "your-API-TOKEN-here"
auth = HTTPBasicAuth("slakshminarayanan.6fs@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first JIRA ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "issuetype": {
      "id": "10005"
      #Navigate to myapp - configure board - issues types - story - you can find the id in URL
    },
    "project": {
      "key": "MYAP"
      #This is the key of your myapp project
    },
    "summary": "My first JIRA Ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
