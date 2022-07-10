import requests
import json

# upload file 
def upload():
    url = "https://app.zeeve.io/zdfs-api/api/v1/file/upload"

    payload={'files': '/app.py',
    'name': 'app.py',
    'isDirectory': 'false'}
    files=[

    ]
    headers = {
        'Authorization': 'Bearer 1829a49867f003274f79ad4f20295f885fca7dc6e89b6d8a'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text, 'hi')

upload()