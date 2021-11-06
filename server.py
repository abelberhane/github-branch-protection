import os
import requests
from flask import Flask, request, abort, logging, json
from urllib3.util import url

app = Flask(__name__)

# This is the service that is listening for the Github Webhook to go off
@app.route('/webhook', methods=['POST'])
def webhook():

    # Here I am creating a dictionary out of the json received from the request
    request_body = request.get_json()
    token = ' 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' #Add your github personal auth token here. Removed each time.
    print(request_body)

    # Here we are assigning variables to the dictionary entries we need
    user = request_body['repository']['owner']['login']
    repo = request_body['repository']['name']


    # Branch Protection Section
    # Only run the branch protection code if the request was a POST method.
    if request.method == 'POST':
        # print(request.json)
        headers = {'Accept': 'application/vnd.github.v3+json'}
        # Here is the json that specifies what type of branch protection we want to apply.
        json_data = '{"required_status_checks":{"strict":true,"contexts":["contexts"]},"enforce_admins":true,"required_pull_request_reviews":null,"restrictions":null}'

        # Below you can see we use the repo variable that was created above to pass the repository that was just created
        payload_url = 'https://api.github.com/repos/abel-org/' + repo + '/branches/main/protection' # Change to master for Official Topps
        response = requests.put(payload_url, headers=headers, data=json_data, auth=(user, token))

        # Here is where I will tackle the creating an issue part
        # First I create a new payload to reflect the URL I need for creating an issue
        payload_url = 'https://api.github.com/repos/abel-org/' + repo + '/issues'
        title = "The main branch has been protected through Github Automation"
        body = "@abelberhane"
        # Once I have a title and a body I store them into item data and encode it into json
        item_data = {'title': title, 'body': body}
        json_data = json.dumps(item_data).encode("utf-8")

        # These are the default headers required per the documentation below:
        # https://docs.github.com/en/rest/reference/issues#create-an-issue
        headers = {'Accept': 'application/vnd.github.v3+json'}
        # Here I send the request to post to the payload URL with teh appropriate headers and our JSON
        response = requests.post(payload_url, headers=headers, data=json_data, auth=(user, token))
        return 'success', 200
    else:
        print("This is not expected")
        abort(400)

if __name__ == '__main__':
    app.run()