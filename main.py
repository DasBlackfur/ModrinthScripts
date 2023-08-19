import json
import os
import shutil
import toml
import re
from side_parse import pw_side_from_mr_env

with open("modrinth.index.json") as readfile:
    modrinth_mods = json.load(readfile)["files"]

shutil.rmtree("mods", ignore_errors=True)
os.mkdir("mods")

for modrinth_mod in modrinth_mods:
    packwiz_mod = {
        "name": re.findall("mods/(.*).jar", modrinth_mod["path"])[0],
        "filename": re.findall("mods/(.*)", modrinth_mod["path"])[0],
        "side": pw_side_from_mr_env(modrinth_mod["env"]),
        "download": {
            "url": modrinth_mod["downloads"][0],
            "hash-format": "sha1",
            "hash": modrinth_mod["hashes"]["sha1"]
        },
        "update": {
            "modrinth": {
                "mod-id": re.findall("data/(.*?)/", modrinth_mod["downloads"][0])[0],
                "version": re.findall("versions/(.*?)/", modrinth_mod["downloads"][0])[0]
            }
        }
    }
    with open("mods/" + packwiz_mod["name"] + ".pw.toml", "w") as writefile:
        toml.dump(packwiz_mod, writefile)

print("Done")
