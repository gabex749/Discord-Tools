import requests
import os
from colorama import init, Fore
import ctypes
import time

init()
ctypes.windll.kernel32.SetConsoleTitleW("Spam Server Channel Tool | Made By gab ex_749")

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
server_id = input(f"{Fore.BLUE}Serveur id : {Fore.RESET}")
channel_id = input(f"{Fore.BLUE}Salon id : {Fore.RESET}")
message = input(f"{Fore.BLUE}Message : {Fore.RESET}")
nb_message =  input(f"{Fore.BLUE}Nombre de messages (écris 0 pour en envoyer à l'infini) : {Fore.RESET}")
s_mode =  input(f"{Fore.BLUE}Secure Mode ? (y/n)) : {Fore.RESET}")

while s_mode != "y" and s_mode != "n":
    print(f"{Fore.RED}❌ Choix incorrecte, choisis y ou n.{Fore.RESET}")
    s_mode = input(f"{Fore.BLUE}Secure Mode ? (y/n)) : {Fore.RESET}")

print(Fore.BLUE + "---------------------------------------------------------" + Fore.RESET)

headers = {'Authorization': token}

if nb_message == "0":
    nb_message = "999999999999"

server_info = requests.get(f"https://discord.com/api/v9/guilds/{server_id}", headers=getheaders(token)).json()
if 'message' in server_info and server_info['message'] == 'Unknown Guild':
    print(f"{Fore.RED}❌ Le serveur spécifié n'existe pas.{Fore.RESET}")
    os.system("pause")
    exit()

channel_info = requests.get(f'https://discord.com/api/v9/channels/{channel_id}', headers=headers).json()
if 'guild_id' not in channel_info or channel_info['guild_id'] != server_id:
    print(f"{Fore.RED}❌ Le salon spécifié n'existe pas ou n'appartient pas au serveur spécifié.{Fore.RESET}")
    os.system("pause")
    exit()

total_m = 0
good_m = 0
bad_m = 0

for i in range(int(nb_message)):
    response = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', data={"content": message}, headers=headers)
    total_m += 1
    if response.status_code == 200:
        print(f"{Fore.GREEN}✅ Message {i} envoyé avec succès.{Fore.RESET}")
        good_m += 1
        if s_mode == "y":
            time.sleep(2)
    else:
        print(Fore.RED + f"❌ Le message {i} n'a pas pu être envoyé. ({response.status_code})" + Fore.RESET)
        time.sleep(2)
        bad_m += 1

print(Fore.BLUE + "---------------------------------------------------------" + Fore.RESET)
print(Fore.WHITE + f"Total : {total_m}  | " + Fore.RED + f"Refusés : {bad_m} | " + Fore.GREEN + f"Envoyés : {good_m}{Fore.RESET}")

os.system("pause")
