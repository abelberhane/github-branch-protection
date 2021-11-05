from flask import Flask, request, abort, logging, json

app = Flask(__name__)

# This is the service that is listening for the Github Webhook to go off
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        # print(request.json)
        return 'success', 200
    else:
        print("This is not expected")
        abort(400)



if __name__ == '__main__':
    app.run()