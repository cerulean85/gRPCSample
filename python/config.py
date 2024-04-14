# import json
# def get_config(path=''):
#     with open(path + "/config.json", "r") as st_json:
#         conf = json.load(st_json)
#     return conf


import yaml
def get_config(path=''):
    with open(path + "/config.yaml", encoding="utf-8") as f:
        yml = yaml.load(f, Loader=yaml.FullLoader)
    return yml