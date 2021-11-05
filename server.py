import os
import requests
from flask import Flask, request, abort, logging, json
from urllib3.util import url

app = Flask(__name__)

# This is the service that is listening for the Github Webhook to go off
@app.route('/webhook', methods=['POST'])
def webhook():

    # Taking the json information we received and putting it into a dictionary
    request_body = request.get_json()
    token = '' #Add your github personal auth token here
    print(request_body)

    # Here we are assigning variables to the dictionary entries we need
    user = request_body['repository']['owner']['login']
    repo = request_body['repository']['name']


    # Branch Protection Section
    # Here we ensure the request is a Post before sending the branch protection Put request
    if request.method == 'POST':
        # print(request.json)
        headers = {'Accept': 'application/vnd.github.v3+json'}
        json_data = '{"required_status_checks":{"strict":true,"contexts":["contexts"]},"enforce_admins":true,"required_pull_request_reviews":null,"restrictions":null}'

        # Below you can see we use the repo variable that was created above to pass the repository that was just created
        payload_url = 'https://api.github.com/repos/abel-org/' + repo + '/branches/main/protection' # Change to master for Official Topps
        response = requests.put(payload_url, headers=headers, data=json_data, auth=(user, token))
        return 'success', 200
    else:
        print("This is not expected")
        abort(400)




if __name__ == '__main__':
    app.run()