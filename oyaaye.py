import requests
from pyfiglet import Figlet
from colorama import Fore, Style, init

# start colorama
init(autoreset=True)

# ASCII title
f = Figlet(font="slant")
print(Fore.GREEN + f.renderText("HANAD HACKER"))

ip = requests.get("https://api.ipify.org").text
print(Fore.GREEN + "PUPLIC IP:", ip)

data = requests.get(f"https://ipinfo.io/{ip}/json").json()

print(Fore.GREEN + "Country:", data.get("country"))
print(Fore.GREEN + "City:", data.get("city"))
print(Fore.GREEN + "Region:", data.get("region"))
print(Fore.GREEN + "Organization:", data.get("org"))
print(Fore.GREEN + "Timezone:", data.get("timezone"))

print(Fore.GREEN + "\nAll data:", data)

print(Fore.GREEN + "\n___________________ALL DATA RESULT SUCCESS_______________")