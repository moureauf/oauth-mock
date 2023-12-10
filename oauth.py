from configparser import ConfigParser
from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)

config = ConfigParser()
config.read('config.ini')
valid_client_id = config.get('OAuth', 'client_id')
valid_client_secret = config.get('OAuth', 'client_secret')
secret_key = config.get('OAuth', 'secret_key')
user_id = config.get('OAuth', 'user_id')
server_port = config.get('server', 'port')

@app.route('/token', methods=['POST'])
def get_token():
    client_id = request.form.get('client_id')
    client_secret = request.form.get('client_secret')
    grant_type = request.form.get('grant_type')

    if not client_id or not client_secret or not grant_type:
        return jsonify({'error': 'Missing required parameters'}), 400
    if client_id == valid_client_id and client_secret == valid_client_secret and grant_type == 'client_credentials':
        token = generate_fake_jwt_token()
        return jsonify({'access_token': token})
    else:
        return jsonify({'error': 'Invalid client credentials or grant_type'}), 401

def generate_fake_jwt_token():
    expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    payload = {
        'sub': user_id,
        'exp': expiration,
    }
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token

if __name__ == '__main__':
    app.run(port=server_port)
