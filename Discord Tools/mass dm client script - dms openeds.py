import requests
import os
from colorama import init, Fore
import ctypes

init()
ctypes.windll.kernel32.SetConsoleTitleW(f"Mass Dm Tool | Made By gab ex_749")

def getheaders(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers

token = input(f"{Fore.BLUE}Token : {Fore.RED}")
os.system("cls")
message = input(f"{Fore.BLUE}Message : {Fore.RESET}")
print(Fore.BLUE + "---------------------------------------------------------" + Fore.RESET)

headers = {'Authorization': token}
channels = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
total_m = 0
good_m = 0
bad_m = 0

for channel in channels:
    channel_id = channel['id']
    channel_info = requests.get(f'https://discord.com/api/v9/channels/{channel_id}', headers=headers).json()
    
    if channel_info['type'] == 1:
        recipient = channel_info['recipients'][0]['username']
        print(f"Envoi du message à @{recipient}...")
        response = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', data={"content": message}, headers=headers)
        total_m += 1
        if response.status_code == 200:
            print(f"{Fore.GREEN}✅ Message envoyé avec succès à @{recipient}.{Fore.RESET}")
            good_m += 1
        else:
            print(Fore.RED + f"❌ Le message n'as pas pue etre envoyé à @{recipient}. ({response.status_code})" + Fore.RESET)
            bad_m += 1

print(Fore.BLUE + "---------------------------------------------------------" + Fore.RESET)
print(Fore.WHITE + f"Total : {total_m}  | " + Fore.RED + f"Refusés : {bad_m} | " + Fore.GREEN + f"Envoyés : {good_m}{Fore.RESET}")

os.system("pause")
