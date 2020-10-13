import os
import argparse
import requests

argp = argparse.ArgumentParser()
argp.add_argument('appid', type=int)
argp.add_argument('key')
args = argp.parse_args()

path = 'data/' + str(args.appid) + '/origin/'

url = 'https://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2/'
params = {'appid': args.appid, 'key': args.key}
with requests.get(url, params) as resp:
    if resp.status_code != 200:
        print(resp.text)
        exit()
    os.makedirs(path, exist_ok=True)
    schema = resp.json()
    for achi in schema['game']['availableGameStats']['achievements']:
        name = achi['name'].lower() + '.jpg'
        print(name)
        with open(path + name, 'wb') as f:
            icon = requests.get(achi['icon']).content
            f.write(icon)