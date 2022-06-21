#! /usr/bin/env python3

# OpenAsar installer by 80xh34d
# Script inspired by OpenAsar batch files

import json
import os
import shutil
import urllib.request
from glob import glob

from scripts.discordutils import DiscordUtils

__github__ = "https://github.com/80xh34d"
__author__ = "boxhead#4466"


class OpenAsar:
    def __init__(self) -> None:
        pass

    def download_openasar(self, path: str) -> None:
        url = "https://github.com/GooseMod/OpenAsar/releases/download/nightly/app.asar"
        urllib.request.urlretrieve(url, path)

    def install(self, client: str) -> None:
        """Installs OpenAsar for the specified client"""
        try:
            path = glob(
                os.path.join(
                    os.getenv("localappdata"), client, "app-*", "resources", "app.asar"
                )
            )[0]
        except IndexError:
            return print(f"-- {client} is not installed.")
        DiscordUtils.kill_discord(client)
        shutil.copy(path, f"{path}.backup")
        self.download_openasar(path)
        print(f"-- Installed OpenAsar")
        DiscordUtils.run_discord(client)

    def uninstall(self, client: str) -> None:
        """Uninstalls OpenAsar from the specified client"""
        try:
            path = glob(
                os.path.join(
                    os.getenv("localappdata"), client, "app-*", "resources", "app.asar"
                )
            )[0]
        except IndexError:
            return print(f"-- {client} is not installed.")
        if not os.path.isfile(f"{path}.backup"):
            return print(f"-- OpenAsar is not installed.")
        DiscordUtils.kill_discord(client)
        shutil.copy(f"{path}.backup", path)
        os.remove(f"{path}.backup")
        try:
            path = glob(DiscordUtils.settings(client))[0]
        except IndexError:
            return print(f"-- settings.json does not exist for {client}")
        with open(path, "r+") as f:
            settings = json.load(f)
            settings.pop("openasar")
            f.seek(0)
            json.dump(settings, f, indent=4)
        print(f"-- Uninstalled OpenAsar")
        DiscordUtils.run_discord(client)


def main() -> None:
    clients = {
        "1": "Discord",
        "2": "DiscordPTB",
        "3": "DiscordCanary",
        "4": "DiscordDevelopment"
    }
    print("Select a client:")
    for id, name in clients.items():
        print(f"\t{id}. {name}")
    client = input("Your choice (1/2/3/4): ")
    if client in clients:
        asar = OpenAsar()
        asar.install(clients[client])

if __name__ == '__main__':
    main()
