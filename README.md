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
To run this Web Server in your organization you will need a few things. First head to [ngrok's](https://ngrok.com/download) website to download this free and simple application hosting web service. Change your directory to this repository once downloaded and run the application with 
```python server.py```
The [documentation for Ngrok](https://ngrok.com/docs) is excellent and once ngrok is running, it's a one line command to have your app up in the web: 
```ngrok http 5000```
Take the URL that is provided in the terminal next to Forwarding and save it for our next step in github. It should look like this "http://1058-66-115-182-68.ngrok.io". Helpful tip, the free tier of ngrok only promises you that URL for 2 hours. Keep that in mind if this is meant for production. 

### Github
You will first need to have created an Organization within Github, and then create a Webhook. When creating the Webhook, Payload URL is going to be the URL that was provided to us in the ngrok application. Change Content type to "application/json" and then make sure to select the events that you would like the webhook to trigger. Perhaps you want it to only act on repository creations or branches being deleted, here is where you select it. 

The last setup step that you will need to complete within Github is to head to your personal settings, developer settings, and then Personal access tokens. You will need to generate a new token and save the output in a secure location. This token is what provides authorization in my script when I attempt to protect the main branch and issue a notification once its complete. In the server.py file you will see a location for you to enter the token that you have created. 

-----------

## Web Service
Through Github's Webhooks documentation, specifically in the [Repository](https://docs.github.com/en/developers/webhooks-and-events/webhooks/webhook-events-and-payloads#repository) section, it specifies which actions can cause an event. Right away we see that created is the first action in the list and the one that we need. I have setup my web server at that address /webhook to accept only POST methods. If the request is a POST method you are allowed to move on to the next section of the code which is protecting the main branch. 


## Protecting the branch
At this point in the code we know that the method is indeed a POST request and begin generating the headers and json data necessary to protect the main branch. Using the python requests library we generate a PUT request to update that branch with the json data from our code. The [documentation](https://docs.github.com/en/rest/reference/repos#update-branch-protection) makes it clear what it's expecting. 


## Issuing a notification
Once the branch is protected in that same if statement, I move on to sending the notification that its been protected. The logic is very similar to what I used with protecting the main branch. I generate the URL and encode the json data needed to send the POST request per the [documentation for creating an issue](https://docs.github.com/en/rest/reference/issues#create-an-issue) and the issue is created. I tagged myself in the body and chose to leave a message in the title letting me know that the branch protection worked. 

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
