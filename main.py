import json
import os
import platform
import shutil
import subprocess
import urllib.request
from glob import glob

import psutil

__github__ = "https://github.com/80xh34d"
__author__ = "boxhead#4466"


class DiscordTools:
    def __init__(self) -> None:
        self.root = os.path.abspath(os.path.join(__file__, os.pardir))
        self.user_os = platform.system()
        self.settings = lambda client: os.path.expanduser(
            {
                "Windows": f"~/AppData/Roaming/{client}/settings.json",
                "Linux": f"~/.config/{client}/settings.json",
                "Darwin": f"~/Library/Application Support/{client}/settings.json",
            }[self.user_os]
        )

    def kill_discord(self, client: str) -> None:
        for proc in psutil.process_iter():
            if client.lower() in proc.name().lower():
                try:
                    proc.kill()
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass

    def run_discord(self, client: str) -> None:
        executable = os.path.join(os.getenv("localappdata"), client, "Update.exe")
        args = f"{executable} --processStart {client}.exe"
        FNULL = open(os.devnull, "w")
        subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=False)

    def enable_dev_console(self, enable: bool = True, client: str = "Discord") -> None:
        """Enables the developer console in Discord's stable client"""
        """paths = {
            "Windows": f"~/AppData/Roaming/{client}/settings.json",
            "Linux": f"~/.config/{client}/settings.json",
            "Darwin": f"~/Library/Application Support/{client}/settings.json"
        }"""
        try:
            path = glob(self.settings(client))[0]
        except IndexError:
            return print(f"-- settings.json does not exist for {client}")
        with open(path, "r+") as f:
            settings = json.load(f)
            settings[
                "DANGEROUS_ENABLE_DEVTOOLS_ONLY_ENABLE_IF_YOU_KNOW_WHAT_YOURE_DOING"
            ] = enable
            f.seek(0)
            json.dump(settings, f, indent=4)
        print(f"-- Enabled {client} developer console")

    def download_openasar(self, path: str) -> None:
        url = "https://github.com/GooseMod/OpenAsar/releases/download/nightly/app.asar"
        urllib.request.urlretrieve(url, path)

    def install_openasar(self, client: str) -> None:
        """Installs OpenAsar for the specified client"""
        try:
            path = glob(
                os.path.join(
                    os.getenv("localappdata"), client, "app-*", "resources", "app.asar"
                )
            )[0]
        except IndexError:
            return print(f"-- {client} is not installed.")
        self.kill_discord(client)
        shutil.copy(path, f"{path}.backup")
        self.download_openasar(path)
        print(f"-- Installed OpenAsar")
        self.run_discord(client)

    def uninstall_openasar(self, client: str) -> None:
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
        self.kill_discord(client)
        shutil.copy(f"{path}.backup", path)
        os.remove(f"{path}.backup")
        try:
            path = glob(self.settings(client))[0]
        except IndexError:
            return print(f"-- settings.json does not exist for {client}")
        with open(path, "r+") as f:
            settings = json.load(f)
            settings.pop("openasar")
            f.seek(0)
            json.dump(settings, f, indent=4)
        print(f"-- Uninstalled OpenAsar")
        self.run_discord(client)

    def main(self) -> None:
        pass
        # self.enable_dev_console(False)
        # self.uninstall_openasar("DiscordPTB")


if __name__ == "__main__":
    tools = DiscordTools()
    tools.main()
