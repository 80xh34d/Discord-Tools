import os
import subprocess
import platform

import psutil


class DiscordUtils:
    def __init__(self) -> None:
        user_os = platform.system()
        self.settings = lambda client: os.path.expanduser(
            {
                "Windows": f"~/AppData/Roaming/{client}/settings.json",
                "Linux": f"~/.config/{client}/settings.json",
                "Darwin": f"~/Library/Application Support/{client}/settings.json",
            }[user_os]
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
