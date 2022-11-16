import hvac
import os
import json
import requests

### Setup environment
VAULT_URL = os.getenv('VAULT_URL')
LOGIN_URL = os.getenv('IICS_LOGIN_URL')
POD_URL =  os.getenv('IICS_POD_URL')

### Could be parameterized in the future for reuse
SECRET_PATH = "bq"
SECRET_NAME = "bq_credentials"
CONNECTION_NAME = "google_de_bigquery_public_data"
TARGET_FIELD = "privateKey"

### Create connection to vault
client = hvac.Client(
    url=VAULT_URL,
    token=os.getenv('VAULT_TOKEN'),
    namespace=os.getenv('VAULT_NAMESPACE'),
)

### Retrieve latest version of secret
bq_credentials = client.secrets.kv.v2.read_secret_version(
    path=SECRET_PATH,
    version=0,
)

### Secret that will replace the current credentials
new_secret = bq_credentials['data']['data'][SECRET_NAME]

### Retrieve informatica login secrets
infa_credentials = client.secrets.kv.v2.read_secret_version(
    path='informatica',
    version=0,
)

infa_user = infa_credentials['data']['data']['login']
infa_pass = infa_credentials['data']['data']['password']

### Login to Informatica ORG
BODY = {"username": infa_user,"password": infa_pass}
login = requests.post(url = LOGIN_URL, json = BODY)
login_json = login.json()

### Get connection ID
HEADERS_V2 = {"Content-Type": "application/json; charset=utf-8", "icSessionId":login_json['userInfo']['sessionId']}
conn = requests.get(POD_URL + "/api/v2/connection/name/" + CONNECTION_NAME, headers = HEADERS_V2)
conn_json = conn.json()

### Update with new secret
conn_json['connParams'][TARGET_FIELD] = new_secret
conn_post = requests.post(POD_URL + "/api/v2/connection/" + conn_json['id'], headers = HEADERS_V2, json = conn_json)
