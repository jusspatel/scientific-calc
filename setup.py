try:
    import pyfiglet
    import subprocess
    import os
    import re
    import sys
    from colorama import * 
    import platform
except ImportError:
    os.system("pip3 install pyfiglet", shell=True)


os.system("cls")

ascii_banner = pyfiglet.figlet_format("Scientific Calc")
print(ascii_banner)
init()
print(Fore.CYAN + " [+] ©Instant Devs Corp. 2020")
print(' ')
print(Fore.CYAN + " [+] Scientific Calc is an advanced calculator")
print(Fore.RED + "-----------------------------------------------------")
print(Fore.WHITE + "App Version : 1.1.0")
print(Fore.WHITE + "Detected OS: " + platform.system())
print(Fore.WHITE + "OS Release: " + platform.release())
print(Fore.RED + "-----------------------------------------------------")
print(Fore.CYAN + "Developer : Juss Patel from Instant Devs Corp.")

input('\n [=] Press Enter to download modules')
print("Please wait")
os.system('pip install mpmath')
print('Modules Installed')

#print(Style.RESET_ALL)


