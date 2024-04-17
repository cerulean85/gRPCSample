# import json
# def get_config(path=''):
#     with open(path + "/config.json", "r") as st_json:
#         conf = json.load(st_json)
#     return conf

import os
current_path = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")

import yaml
def get_conf():
    with open(f"{current_path}/config.yaml", encoding="utf-8") as f:
        yml = yaml.load(f, Loader=yaml.FullLoader)
    return yml

def get_server_conf(target=None):
    conf = get_conf()
    if target == None:
        return conf["server"]
    return conf["server"][target]

def get_storage_conf(target=None):
    conf = get_conf()
    if target == None:
        return conf["storage"]
    return conf["storage"][target]
