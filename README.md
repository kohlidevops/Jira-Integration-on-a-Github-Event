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




