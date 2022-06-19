import json
import os
import platform
import shutil

import psutil

__github__ = "https://github.com/80xh34d"
__author__ = "boxhead#4466"


class DiscordTools:
    def __init__(self) -> None:
        self.root = os.path.abspath(os.path.join(__file__, os.pardir))
        self.user_os = platform.system()

    def kill_discord(self, client: str) -> None:
        for proc in psutil.process_iter():
            if any(procstr in proc.name().lower() for procstr in client.lower()):
                try:
                    proc.kill()
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass

    def enable_dev_console(self, enable: bool = True) -> None:
        """ Enables the developer console in Discord's stable client """
        paths = {
            "Windows": "~/AppData/Roaming/discord/settings.json",
            "Linux": "~/.config/discord/settings.json",
            "Darwin": "~/Library/Application Support/Discord/settings.json"
        }
        path = os.path.expanduser(paths[self.user_os])
        if not os.path.isfile(path):
            return
        with open(path, "r+") as f:
            settings = json.load(f)
            settings["DANGEROUS_ENABLE_DEVTOOLS_ONLY_ENABLE_IF_YOU_KNOW_WHAT_YOURE_DOING"] = enable
            f.seek(0)
            json.dump(settings, f, indent=4)
        print('-- Enabled Discord developer console')

    def install_openasar(self, client: str) -> None:
        """ Installs OpenAsar for the specified client """
        target = os.path.join(os.getenv('localappdata'), client)
        if not os.path.isdir(target):
            return
        self.kill_discord(client)
        shutil.copy()

        path = os.path.join(self.root, "scripts", f"{client}.bat")
        with open(path, "r") as f:
            script = f.read().splitlines()
        for line in script:
            os.system(line)
        print("\n-- Installed OpenAsar")

    def main(self) -> None:
        self.enable_dev_console(False)
        # self.install_openasar('discord')


if __name__ == '__main__':
    tools = DiscordTools()
    tools.main()
