import requests
import os
import shutil
import colorama
import time
import json

from json import load
from colorama import Fore, Back, Style

UI = """
      ____ _   _________  ____________  _______
     / __ \ | / / __/ _ \/_  __/  _/  |/  / __/
    / /_/ / |/ / _// , _/ / / _/ // /|_/ / _/  
    \____/|___/___/_/|_| /_/ /___/_/  /_/___/ 
                                            \n"""


os.system("cls")
token = load(open('config.json'))["token"]
os.system("cls")

def main():
    if __name__ == "__main__":
        guilds = requests.get("https://discord.com/api/v9/users/@me/guilds", headers={"authorization": token}).json()
        i = 0
        msg = ""
        server_ids = []
        server_names = []
        for guild in guilds:
            i += 1
            server_ids.append(guild["id"])
            server_names.append(guild["name"])
            msg += f"   {Fore.YELLOW}[{Fore.RESET}{str(i)}{Fore.YELLOW}]{Fore.RESET} " + guild["name"] + "\n"

        os.system(f"title Discord Stealer Emoji - By Timmy")
        print(UI)
        print(msg)
        server = input(f"   [+] Choose: ")
        if server.isdigit():
            server_id = server_ids[int(server) + -1]
            server_name = server_names[int(server) + -1]
        else:
            print("   not a num")
            main()
        server_folder = restrict(server_name)
        if os.path.isdir("./" + server_folder):
            print("   removing the folder " + server_folder)
            shutil.rmtree("./" + server_folder)
        os.mkdir("./" + server_folder)
        
        os.system("cls")
        print()
        print("   Download emoji in discord server " + (Fore.YELLOW + server_name + "\n"))

        emojis = requests.get("https://discord.com/api/v9/guilds/" + server_id + "/emojis", headers={"authorization": token}).json()
        i = 0
        for emoji in emojis:
            i += 1
            if emoji["animated"]:
                with open("./" + server_folder + "/" + emoji["name"] + ".gif", "wb") as f:
                    print(f"   {Fore.RED}[{Fore.GREEN}download{Fore.RED}]{Fore.RESET} " + emoji["name"] + " (animated) (" + str(i) + "/" + str(len(emojis)) + ")")
                    f.write(requests.get("https://cdn.discordapp.com/emojis/" + emoji["id"] + ".gif?v=1").content)
            else:
                with open("./" + server_folder + "/" + emoji["name"] + ".png", "wb") as f:
                    print(f"   {Fore.RED}[{Fore.GREEN}download{Fore.RED}]{Fore.RESET} " + emoji["name"] + " (" + str(i) + "/" + str(len(emojis)) + ")")
                    f.write(requests.get("https://cdn.discordapp.com/emojis/" + emoji["id"] + ".png?v=1").content)
        
        os.system("cls")
        print()
        print("   finished downloading all emojis " + (Fore.YELLOW + server_name + Fore.RESET))
        time.sleep(1)
        os.system("cls")
        main()

def restrict(str_):
    if os.name == "nt":
        str_ = str_.translate({ord(i): None for i in '\/:*?"<>|'})
    else:
        str_ = str_.replace("/", "")
    if len(str_) == 0:
        str_ = "no name"
    return str_

if __name__ == "__main__":
    main()