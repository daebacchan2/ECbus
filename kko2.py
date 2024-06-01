import requests
import json

with open("kakao_code.json","r") as fp:
    tokens = json.load(fp)

url="https://kapi.kakao.com/v2/api/talk/memo/default/send"

# kapi.kakao.com/v2/api/talk/memo/default/send

headers={
    "Authorization" : "Bearer " + tokens["access_token"]
}

data={
    "template_object": 108039}

response = requests.post(url, headers=headers, data=data)
print(response.status_code)
