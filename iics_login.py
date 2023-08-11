import requests
import json
from datetime import timedelta
from datetime import datetime,timedelta


def iics_v2_login( username: str, password: str):
        
    login_url = 'https://dm-us.informaticacloud.com/ma/api/v2/user/login'       
# Prepare request header
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json' }

    # Prepare request body
    body = json.dumps( {
        "@type": "login",
        "username": username,
        "password": password } )

    # Log into IICS
    response = requests.post(login_url, headers=headers, data=body)

    # Inspect some attributes of the `requests response
    json_response = response.json()
    server_url = json_response['serverUrl']
    icSessionId = json_response['icSessionId']

       
    # Extract connection information
    return server_url, icSessionId, json_response


def iics_server_url(method:str,server_url,iics_v2_session_id):
        
    payload={}
    headers = {
      'Content-Type': 'application/json',
      'INFA-SESSION-ID': iics_v2_session_id
    }
    
    response = requests.request(method, server_url, headers=headers, data=payload)
    return response.json()