# github-branch-protection

GitHub has a powerful API that enables developers to easily access GitHub data.

## Goals##:
1) Create a simple web service that listens for organization events to know when a repository has been created.
2) When the repository is created please automate the protection of the main branch.
3) Notify yourself with an @mention in an issue within the repository that outlines the protections that were added.

----------------------

## Web Service##
Through Github's Webhooks documentation, specifically in the [Repository](https://docs.github.com/en/developers/webhooks-and-events/webhooks/webhook-events-and-payloads#repository) section, it specifies which actions can cause an event. Right away we see that created is the first one and the one that we need. 













*Sources*:
  * https://docs.github.com/en/developers/webhooks-and-events/webhooks/webhook-events-and-payloads#repository

Github Organization - https://github.com/abel-org
