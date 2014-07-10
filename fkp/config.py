import os, json

VALID_CONFIG_PATHS = [
    "~/.fk",
]

CONFIG = {}

def load_config():
    global CONFIG
    for path in VALID_CONFIG_PATHS:
        if os.path.exists(os.path.expanduser(path)):
            CONFIG = json.load(open(path, "r"))
