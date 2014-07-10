import os, lupa

VALID_SCRIPT_PATHS = [
    "~/.fk.scripts",
]

CACHED_SCRIPTS = {}

def load_scripts():
    for path in VALID_SCRIPT_PATHS:
        if os.path.exists(os.path.expanduser(path)):
            CACHED_SCRIPTS[path] = Script(open(path, "r").read())

class Script(object):
    def __init__(self, src):
        self.src = src
        self.r = lupa.LuaRuntime()

    def run(self):
        return self.r.execute(self.src)

class APIMixin(object): pass
