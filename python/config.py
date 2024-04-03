import json
def get_config(path=''):
    with open(path + "/config.json", "r") as st_json:
        conf = json.load(st_json)
    return conf
