from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__)
@app.route('/createjira', methods=['POST'])
def createJIRA():


    url = "https://slakshminarayanan.atlassian.net/rest/api/3/issue"
    API_TOKEN = "your-API_TOKEN-here"
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
    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
if __name__ == '__main__':
    app.run("0.0.0.0", port=5000)
