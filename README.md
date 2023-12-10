# OAuth Mock Server

This simple Flask app serves as a mock OAuth server implementing the Client Credentials flow. It generates a fake JWT access token for valid client credentials.

## Prerequisites

- [Python 3.x](https://www.python.org/)
- Pip (Python package installer)

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/moureauf/oauth-mock.git
    cd oauth-mock
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

Update the `config.ini` file with your OAuth configuration:

```ini
[OAuth]
client_id = yourClientId
client_secret = yourClientSecret
secret_key = yourSecretKey
user_id = yourUserId

[server]
port = 5000
```

## Running the Server

Run the Flask app:

```bash
python oauth.py
```

The OAuth server will be accessible at `http://127.0.0.1:5000`.

## Obtaining an Access Token

Make a `POST` request to `http://127.0.0.1:5000/token` with the following parameters:

- `client_id`: Your client ID
- `client_secret`: Your client secret
- `grant_type`: 'client_credentials'

Example using curl:

```bash
curl -X POST -d "client_id=yourClientId&client_secret=yourClientSecret&grant_type=client_credentials" http://127.0.0.1:5000/token
```

The server will respond with a JSON containing the access token.

## Error Handling

The server handles missing or invalid parameters gracefully and responds with appropriate error messages.

### Note:

- This is a simple mock server for educational purposes.
- In a production environment, consider securing sensitive information better.
- Do not use fake or weak secrets in real-world scenarios.

Feel free to customize the code and structure according to your needs.
