import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = 'e67be30a23f5c66ad59c13e4f7f10c63'
redirect_uri = 'https://example.com/oauth'
authorize_code = '4C--9_AXwi6RCsrSTePB3BxpoVw93my6NJGA6TEApRO74LbBKlwZpAAAAAQKKiVRAAABj4sWjzwq17LwdM8QAg'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# json 저장
import json

with open("kakao_code.json","w") as fp:
    json.dump(tokens, fp)