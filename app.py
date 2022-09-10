import requests as r
import bs4 as bs
import time
from colorama import Fore, Back, Style

banner = """

░██████╗██╗░░░██╗██████╗░██╗░░██╗████████╗██████╗░░█████╗░░█████╗░████████╗░█████╗░██████╗░
██╔════╝██║░░░██║██╔══██╗╚██╗██╔╝╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
╚█████╗░██║░░░██║██████╦╝░╚███╔╝░░░░██║░░░██████╔╝███████║██║░░╚═╝░░░██║░░░██║░░██║██████╔╝
░╚═══██╗██║░░░██║██╔══██╗░██╔██╗░░░░██║░░░██╔══██╗██╔══██║██║░░██╗░░░██║░░░██║░░██║██╔══██╗
██████╔╝╚██████╔╝██████╦╝██╔╝╚██╗░░░██║░░░██║░░██║██║░░██║╚█████╔╝░░░██║░░░╚█████╔╝██║░░██║
╚═════╝░░╚═════╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
"""

print(Fore.RED +banner)
print(Fore.WHITE+"="*60)
print(Fore.WHITE+f"\t[+] Created by","anukulpandey","[+] ")
print("\t[!] TOOL : SubXtractor [!]")
print("\tThe only tool you need for subdomains lookup")
print(Fore.WHITE+"="*60)
print("Enter the url you want to extract domains from",end="")
url = input()
# https://subdomainfinder.c99.nl/scans/2022-09-08/bcc.nl

sourceCode = r.get(f'{url}').content
results = bs.BeautifulSoup(sourceCode,'html5lib')

hostName = url.split('/')[-1].split('.')[0]
print(hostName)
file_object = open('op.txt', 'a')

def subdomain_checker(url):
    subdSplit = url.split('/')
    dotSplit = subdSplit[-1].split('.')

    if hostName in dotSplit:
        if(subdSplit[-1]!=f'{hostName}.{dotSplit[-1]}'):
            print(subdSplit[-1])
            file_object.write(f'{subdSplit[-1]}\n')
            
        
for i in results.find_all('a'):
    try:
        subdomain_checker(i['href'])
    except Exception as e:
        pass

print("Saved output in op.txt")
