import requests
import json

# upload a file 
def upload(file, filename):
    url = "https://app.zeeve.io/zdfs-api/api/v1/file/upload"

    payload={
    'files': 'file',
    'name': 'filename',
    'isDirectory': 'false'}
    files=[

    ]
    headers = {
        'Authorization': 'Bearer d5edea4f4c1341d7daacec386e43746d2ee76082518b6b1b'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)

upload()