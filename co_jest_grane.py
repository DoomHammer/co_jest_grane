import requests

r = requests.get('https://raw.githubusercontent.com/DoomHammer/co_jest_grane/master/ready')
payload = r.json()

print(payload['text'])
