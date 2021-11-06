# Github Branch Protection

GitHub has a powerful API that enables developers to easily access GitHub data.

Please create a simple web service that listens for organization events to know when a repository has been created. When the repository is created please automate the protection of the main branch. Notify yourself with an @mention in an issue within the repository that outlines the protections that were added.

--------------------

## Goals:
1) Create a simple web service that listens for organization events to know when a repository has been created.
2) When the repository is created please automate the protection of the main branch.
3) Notify yourself with an @mention in an issue within the repository that outlines the protections that were added.

----------------------

## Setup
### Ngrok Web Server
To run this Web Server in your organization you will need a few things. First head to [ngrok's](https://ngrok.com/download) website to download this free and simple application hosting web service. The [documentation](https://ngrok.com/docs) is excellent and once ngrok is open, it's a one line command to have your app up in the web. 
```ngrok http 5000```
Take the URL that is provided in the terminal next to Forwarding and save it for our next step in github. It should look like this "http://1058-66-115-182-68.ngrok.io". Helpful tip, the free version of ngrok only promises you that URL for 2 hours. Keep that in mind if this is meant for production. 

### Github
You will first need to have created an Organization within Github, and then create a Webhook. When creating the Webhook, Payload URL is going to be the URL that was provided to us in the ngrok application. Change Content type to "application/json" and then make sure to select the events that you would like the webhook to trigger. Perhaps you want it to only act on repository creations or branches being deleted, here is where you select it. 

The last setup step that you will need to complete within Github is to head to your personal settings, developer settings, and then Personal access tokens. You will need to generate a new token and save the output in a secure location. This token is what provides authorization in our scripts when we attempt to protect the main branch and issue a notification once its complete. In the server.py file you will see a location for you to enter the token that you have created. 

-----------

## Web Service
Through Github's Webhooks documentation, specifically in the [Repository](https://docs.github.com/en/developers/webhooks-and-events/webhooks/webhook-events-and-payloads#repository) section, it specifies which actions can cause an event. Right away we see that created is the first one and the one that we need. Change the content type to application/json 



## Protecting the branch


## Issuing a notification




----------------------
*Sources*:
  * https://www.youtube.com/watch?v=HQLRPWi2SeA&t=75s
  * https://docs.github.com/en/developers/webhooks-and-events/webhooks/webhook-events-and-payloads#repository
  * https://docs.github.com/en/rest/reference/repos#update-branch-protection
  * https://docs.github.com/en/rest/reference/issues#create-an-issue
  * https://youtu.be/b_DVXgiByec
  * https://www.youtube.com/watch?v=S9cjO6V7EXg
  * https://www.thepythoncode.com/article/webhooks-in-python-with-flask
  * https://ngrok.com/docs
----------------------

Github Organization - https://github.com/abel-org
