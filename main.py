import json
import os
from glob import glob

from scripts.openasar import OpenAsar
from scripts.discordutils import DiscordUtils

__github__ = "https://github.com/80xh34d"
__author__ = "boxhead#4466"


class DiscordTools:
    def __init__(self) -> None:
        self.root = os.path.abspath(os.path.join(__file__, os.pardir))

    def exit(self) -> None:
        print("-- Goodbye!")
        raise SystemExit

    def clear(self) -> None:
        os.system("cls" if os.name in ("nt", "dos") else "clear")

    def enable_dev_console(self, enable: bool = True, client: str = "Discord") -> None:
        """Enables the developer console in Discord's stable client"""
        try:
            path = glob(DiscordUtils.settings(client))[0]
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

    def main(self) -> None:
        choices = {
            "1": self.enable_dev_console,
            "2": self,
            "3": self,
            "4": OpenAsar,
            "5": self,
            "6": self.exit
        }
        while True:
            self.clear()
            print("-------------------------------")
            print(" / Discord Tools Menu v1.0.0 \ ")
            print(" \   Coded by Boxhead#4466   / ")
            print("-------------------------------\n")
            print("Found clients -")
            print("Discord, DiscordPTB, DiscordCanary")
            print("\n~/tools/main")
            print("\t1. Developer Console")
            print("\t2. Clear Cache")
            print("\t3. Clear Local Storage")
            print("\t4. OpenAsar")
            print("\t5. Info")
            print("\t6. Exit")
            c = input("Choice [1|2|3|4|5|6]: ")
            if c in "123456":
                break
        choices[c]()
        # OpenAsar("Discord").install()
        # self.enable_dev_console(False)
        # self.uninstall_openasar("DiscordPTB")


if __name__ == "__main__":
    tools = DiscordTools()
    tools.main()
