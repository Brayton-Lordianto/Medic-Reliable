import requests
import json

# upload a file 
def upload(file, filename, auth):
    url = "https://app.zeeve.io/zdfs-api/api/v1/file/upload"

    payload={
    'files': f"file",
    'name': f"filename",
    'isDirectory': 'false'}
    files=[

    ]
    headers = {
        'Authorization': f"Bearer {auth}"
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)
