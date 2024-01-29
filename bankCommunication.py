from flask import Flask, request, jsonify
import requests
import json
import os

app = Flask(__name__)

@app.route('/sendToBankHostSimulator2', methods=['POST'])
def handle_transaction():
    try:
        request_body = request.get_json()


        # API URL for Docker
        api_url = "http://host.docker.internal:8088/api/v1/transactions/processTransaction"

        # API URL for localhost
        #api_url = "http://localhost:8088/api/v1/transactions/processTransaction"

        json_body = json.dumps(request_body)
        headers = {'Content-Type': 'application/json'}

        response = requests.post(api_url, data=json_body, headers=headers)
        print("json", json_body)
        
        print("Header", headers)
        print(response)

        return response.text, response.status_code

    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=8087 )
