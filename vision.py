#Vision Bot by Hoshea Yarden

import json
import requests
requests.packages.urllib3.disable_warnings()

url = "https://127.0.0.1:2999/liveclientdata/playerlist"
champions = []
vision = []
def checkVision():
    req = requests.get(url, verify=False)
    for line in str(req.text).split('\n'):
        if '\"championName\":' in line:
            champions.append(line.split(':')[1].strip().split('\"')[1].strip('\"'))
        if '\"wardScore\":' in line:
            vision.append(line.split(':')[1].strip())
try:
    checkVision()
    for i in range(len(champions)):
        print(f"Champion: {champions[i]}\nVision Score: {vision[i]}\n")
    print(champions)
    print(vision)
except Exception as e:
    print("Start a game first")
    print(e)

