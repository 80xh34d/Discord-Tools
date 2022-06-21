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

    def snowflake_to_date(snowflake: int) -> str:
        timestamp = ((snowflake >> 22) + 1420070400000) / 1e3
        print(timestamp)
        return timestamp

    def kill_discord(client: str) -> None:
        for proc in psutil.process_iter():
            if client.lower() in proc.name().lower():
                try:
                    proc.kill()
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass

    def run_discord(client: str) -> None:
        executable = os.path.join(os.getenv("localappdata"), client, "Update.exe")
        args = f"{executable} --processStart {client}.exe"
        FNULL = open(os.devnull, "w")
        subprocess.call(args, stdout=FNULL, stderr=FNULL, shell=False)

DiscordUtils.snowflake_to_date(988546298540085298)