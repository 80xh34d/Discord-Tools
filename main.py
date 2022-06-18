import os
import json
import subprocess
import platform

__github__ = "https://github.com/80xh34d"
__author__ = "boxhead#4466"


class DiscordTools:
    def __init__(self) -> None:
        pass

    def enable_dev_console(self) -> None:
        """ Enables the developer console in Discord's stable client """
        paths = {
            "Windows": "~/AppData/Roaming/discord/settings.json",
            "Linux": "~/.config/discord/settings.json",
            "Darwin": "~/Library/Application Support/Discord/settings.json"
        }
        path = os.path.expanduser(paths[platform.system()])
        if not os.path.isfile(path):
            return
        with open(path, "r+") as f:
            settings = json.load(f)
            settings["DANGEROUS_ENABLE_DEVTOOLS_ONLY_ENABLE_IF_YOU_KNOW_WHAT_YOURE_DOING"] = True
            f.seek(0)
            json.dump(settings, f, indent=4)
        print('-- enabled discord developer console')

    def install_openasar(self, client: str) -> None:
        """ Installs OpenAsar for the specified client """

        pass

    def main(self) -> None:
        self.enable_dev_console()


if __name__ == '__main__':
    tools = DiscordTools()
    tools.main()
