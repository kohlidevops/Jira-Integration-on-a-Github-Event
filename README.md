# How to Automate JIRA creation on a Github Event using Python

## Why do we need JIRA integration on a Github event?

Integrating JIRA with GitHub events streamlines project management and fosters collaboration, enhancing overall efficiency and transparency in the development process.

## What problem statement has given to DevOps team by Development team?

![image](https://github.com/kohlidevops/Jira-Integration-on-a-Github-Event/assets/100069489/1f26e304-d427-4c5d-a369-0e94635aa28d)

1. When QE team or someone find the bugs, then they raised the issues in Github.
2. Then some one of developer team will check the rasied issues.
3. If this raised issues are not valid then developer will close this ticket.
4. If this issues are valid, then developer will create a JIRA ticket.
5. Now, Developer team will ask help from DevOps team that whether we can automate this process? - So, When developer open this ticket from Github, then automatically this raised issues need to send with details to JIRA.

## JIRA creation

To signup with JIRA with below link

```
https://team.atlassian.com/your-work
```

![image](https://github.com/kohlidevops/Jira-Integration-on-a-Github-Event/assets/100069489/8d8670c9-4085-4ca2-b784-ebddc7184b9c)

Create a new project using view all project - Create a new project - Select - Scrum - Use template

![image](https://github.com/kohlidevops/Jira-Integration-on-a-Github-Event/assets/100069489/a2c213d4-b363-436a-84f1-c3c38da0e32c)

Then select a team-managed project - Add project details

![image](https://github.com/kohlidevops/Jira-Integration-on-a-Github-Event/assets/100069489/0c0cf2af-d182-4625-8dd9-e145a4d86691)

### To create API token in JIRA

Navigate to account - profile - Manage your account

![image](https://github.com/kohlidevops/Jira-Integration-on-a-Github-Event/assets/100069489/369cc994-3414-4481-8840-300c601b282e)

Select - security - create and manage API tokens - create a API token (Copy it for later use)

![image](https://github.com/kohlidevops/Jira-Integration-on-a-Github-Event/assets/100069489/2e22fcd7-1ceb-4f92-9ca5-4c7d0e79bd57)

#### Example - Try to get all projects from JIRA using python code with API

You can get this code using below link - select - Python - copy the code

```
https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-projects/#api-group-projects
```

Open Github code space and create a project and start work on it.

Replace the URL, email-id and API token in the python code with your atlassian name

```
url = "https://slakshminarayanan.atlassian.net/rest/api/3/project"
```

You can use below link to get updated python code

```
https://github.com/kohlidevops/Jira-Integration-on-a-Github-Event/blob/main/list-all-projects-from-jira
```

### Create a Issue in Jira using python code

You can get this code using below link

```
https://github.com/kohlidevops/Jira-Integration-on-a-Github-Event/blob/main/create_issue.py
```

Now go to github code space and create new file and copy paste this code and run it again.

![image](https://github.com/kohlidevops/Jira-Integration-on-a-Github-Event/assets/100069489/2292737f-8a9f-4ac9-bb5f-d1add4d399d4)

Perfect! Its running. Now I had a quick look at the JIRA

JIRA - myapp (project) - Backlog - you can see the new issue has been created.

![image](https://github.com/kohlidevops/Jira-Integration-on-a-Github-Event/assets/100069489/769d612d-7f82-4ee4-a84c-38a5d97ddae5)

## JIRA and Github Integration

![image](https://github.com/kohlidevops/Jira-Integration-on-a-Github-Event/assets/100069489/f4ec961b-460a-495d-a2f6-624056e10d52)

Launch ubuntu EC2 instance with t2.micro and SSH into machine.

Install below commands to make ready state - Python3 has been installed already on ubuntu22

```
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install pip -y
pip3 install flask
```

create a hello-world application

You can use below link to run the application

```
https://github.com/kohlidevops/Jira-Integration-on-a-Github-Event/blob/main/hello-world.py
```

Now you can run this application

```
python3 hello-world.py
```

![image](https://github.com/kohlidevops/Jira-Integration-on-a-Github-Event/assets/100069489/82f2eaf6-0907-472a-a072-5c172db4f731)

It has been running!

![image](https://github.com/kohlidevops/Jira-Integration-on-a-Github-Event/assets/100069489/22091b20-b49c-44e1-b510-c2784301e33c)

### To run JIRA flask application

To update the code and run the flask application using below code

```
from flask import Flask
import requests
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__)
@app.route('/createjira', methods=['POST'])
def createJIRA():


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
    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
if __name__ == '__main__':
    app.run("0.0.0.0", port=5000)
```

### To create a Github webhooks for flask application

Github -kohlidevops/Jira-Integration-on-a-Github-Event - Settings - Webhooks - Add Webhook

```
payload url - http://ec2-13-127-94-143.ap-south-1.compute.amazonaws.com:5000/createjira
content type - application/json
choose - Let me select individual events - Issue comments - Add webhook
```

![image](https://github.com/kohlidevops/Jira-Integration-on-a-Github-Event/assets/100069489/a242129a-dbb9-45c1-9e44-9cf95a53a2e6)

#### Make ensure you have added API token and Http auth in github-jira.py file

#### I have updated webhook as createjira

After adding webhook you can refer the manage webhook to ensure whether its ping or not

![image](https://github.com/kohlidevops/Jira-Integration-on-a-Github-Event/assets/100069489/5e60e7f2-4cf4-4772-b2ec-9799c1baed11)

### To create an Issue

Navigate to github 
```
https://github.com/kohlidevops/Jira-Integration-on-a-Github-Event
```
Create an Issue - Submit new issues

### To create an comment

Navigate to the respective issues and comment it to ensure this Issues has been sent to jira.

![image](https://github.com/kohlidevops/Jira-Integration-on-a-Github-Event/assets/100069489/5336dd1f-cdca-4b66-83c6-4f5a4f5d79de)

Perfect! Jira ticket has been created. Just check with Atlassian Jira - Projects - myapp - Backlog

![image](https://github.com/kohlidevops/Jira-Integration-on-a-Github-Event/assets/100069489/cc5150a8-75c5-40a9-b3d6-aa8a0ce3000e)

That's it!
