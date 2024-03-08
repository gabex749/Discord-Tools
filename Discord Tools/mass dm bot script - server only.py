import os
import discord
from discord.ext import commands
from colorama import init, Fore
import ctypes
import time

init()
intents = discord.Intents().all()
bot = commands.Bot(command_prefix="/", intents=intents)
client = discord.Client(intents=intents)
ctypes.windll.kernel32.SetConsoleTitleW(f"Mass Dm Tool | Made By gab ex_749")

token = input(f"{Fore.BLUE}Token : {Fore.RED}")
os.system("cls")
invisible_mode = input(f"{Fore.BLUE}Activer le mode invisible ? (y/n) : {Fore.RESET}")

while invisible_mode.lower() not in ['y', 'n']:
    os.system("cls")
    print(f"{Fore.RED}Veuillez entrer 'y' pour Oui ou 'n' pour Non.{Fore.RESET}")
    invisible_mode = input(f"{Fore.BLUE}Activer le mode invisible ? (y/n) : {Fore.RESET}")

@bot.event
async def on_ready():
    
    if invisible_mode == "y":
        await bot.change_presence(status=discord.Status.invisible)
        print(Fore.GREEN + "✅ Mode invisible activé." + Fore.RESET)
        time.sleep(1)

    os.system("cls")
    print(Fore.GREEN + "✅ Le bot s'est bien connecté !" + Fore.RESET)
    time.sleep(1)
    print(Fore.BLUE + "Récupèration des serveurs..." + Fore.RESET)
    time.sleep(1)
    servers = bot.guilds

    if len(servers) == 0:
        os.system("cls")
        print(Fore.RED + "❌ Le bot n'est dans aucun serveur." + Fore.RESET)
        return

    for server in servers:
        print(Fore.RESET + f"Nom du serveur : {server.name}, {server.id}")
        print(Fore.BLUE + "---------------------------------------------------------" + Fore.RESET)

    time.sleep(1)
    choice_server_id = input(f"{Fore.BLUE}Id du serveur sur lequel mass dm : {Fore.RESET}")

    try:

        chosen_server = discord.utils.get(bot.guilds, id=int(choice_server_id))
        message = input(f"{Fore.BLUE}Entre le message que tu veux envoyer à tout le monde : {Fore.RESET}")
        print(Fore.BLUE + "---------------------------------------------------------" + Fore.RESET)
        m_count = 0
        m_good = 0
        m_bad = 0

        for member in chosen_server.members:
            m_count += 1
            ctypes.windll.kernel32.SetConsoleTitleW(f"Mass Dm Tool | Made By gab ex_749 | Running, member : {m_count}, target: @{member.name} | Server: {chosen_server.name}")
            try:
                await member.send(message)
                print(Fore.GREEN + f"✅ Message envoyé à {member.name}#{member.discriminator} en DM." + Fore.RESET)
                m_good += 1
            except:
                print(Fore.RED + f"❌ {member.name} à ses DM de fermés." + Fore.RESET)
                m_bad += 1
    except Exception as e:
        print(Fore.RED + f"❌ L'id du serveur est invalide, ou en tout cas, une erreur est survenue : {e}" + Fore.RESET)
    
    print(Fore.BLUE + "---------------------------------------------------------" + Fore.RESET)
    print(Fore.WHITE + f"Total : {m_count}  | " + Fore.RED + f"Refusés : {m_bad} | " + Fore.GREEN + f"Envoyés : {m_good}")

try:
    bot.run(token=token)
    os.system("cls")
except Exception as e:
    os.system("cls")
    print(Fore.RED + f"❌ Le script n'as pas réussi à se connecter au bot. ({e})" + Fore.RESET)

os.system("pause")