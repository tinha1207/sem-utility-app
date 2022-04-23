import requests
import logging


endpoint = "http://localhost:8001/account/"

def test_account():
    payload = {     
    "account": "string",
    "platform": "string",
    "sales_channel_id": 0,
    "country_code": "ZZ",
    "prefix": "string"
    }

    payload2 = {
        "account": "string",
        "platform": "string",
        "sales_channel_id": 1,
        "country_code": "ZZ",
        "prefix": "string"
    }

    r = requests.post(
        url=endpoint,
        json=payload,

    )
    assert r.status_code == 201
    response = r.json()
    
    
    g = requests.get(
        url = f'{endpoint}{response["id"]}'
    )
    assert g.status_code == 200

    u = requests.put(
        url=f"{endpoint}{response['id']}",
        json=payload2
    )

    assert u.status_code == 200
    

    d = requests.delete(
        url = f'{endpoint}{response["id"]}'
    )
    assert d.status_code == 204
    

    


