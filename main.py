# Программа написана программистом @Opasniy_chel (Telegram)
import sys
import os
from time import sleep
import importlib
try:
    print(sys.version)
    def program(): #Программа
        modules = ['requests', 'colorama']
        for module in modules:
            try:
                importlib.import_module(module)
            except:
                print(f'Вы не установили модуль {module}')
                exit(0)
        from colorama import init, Fore
        init(autoreset=True)
        print(Fore.BLUE + 'Программа написана программистом @Opasniy_chel (Telegram)')
        print(Fore.MAGENTA + '''███████ ██ ████████ ███████ 
██      ██    ██    ██      
███████ ██    ██    █████   
     ██ ██    ██    ██      
███████ ██    ██    ███████\n''')
        print(Fore.LIGHTYELLOW_EX + '''██    ██  █████  ██      ██ ██████  
██    ██ ██   ██ ██      ██ ██   ██ 
██    ██ ███████ ██      ██ ██   ██ 
 ██  ██  ██   ██ ██      ██ ██   ██ 
  ████   ██   ██ ███████ ██ ██████  
                                    ''')
        print(Fore.LIGHTMAGENTA_EX + '''██████ ██   ██ ███████  ██████ ██   ██ ███████ ██████  
██      ██   ██ ██      ██      ██  ██  ██      ██   ██ 
██      ███████ █████   ██      █████   █████   ██████  
██      ██   ██ ██      ██      ██  ██  ██      ██   ██ 
 ██████ ██   ██ ███████  ██████ ██   ██ ███████ ██   ██ 
                                                        ''')
        from check_site import check_site
        sleep(1)
        print(Fore.BLUE + 'Программа написана программистом @Opasniy_chel (Telegram)')
        input(Fore.LIGHTCYAN_EX + 'Для продолжения нажмите Enter > ')
        site = input('\nВведите адрес сайта https://')
        check_site(site)
    program()
except:
    sleep(2)
    os.startfile('main.py')
# Программа написана программистом @Opasniy_chel (Telegram)