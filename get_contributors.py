import toml
import requests
from glob import glob

mods: list[str] = glob("mods/*.pw.toml")
contributors: set[str] = set()

for mod in mods:
    mod_info = toml.load(mod)
    try:
        mod_id = mod_info["update"]["modrinth"]["mod-id"]
        mod_contributors = requests.get(f"https://api.modrinth.com/v2/project/{mod_id}/members").json()

        for mod_contributor in mod_contributors:
            contributors.add(mod_contributor["user"]["username"])

    except KeyError:
        print(f"Mods from sources other than Modrinth are not supported! ({mod_info["name"]} could not be found)")

contributor_string = ", ".join(contributors)
print(contributor_string)