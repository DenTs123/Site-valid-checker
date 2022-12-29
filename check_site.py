# Пожалуйста не трогайте этот скрипт
# Программа написана программистом @Opasniy_chel (Telegram)
import requests
import colorama
from colorama import init, Fore
init(autoreset=True)
def check_site(url): # Проверка сайта на валидность
    try:
        check_site = requests.get('https://' + url)
        if check_site.status_code:
            print(Fore.LIGHTGREEN_EX + 'Сайт работает\n'
                 f'Код: {check_site.status_code}\n'
                  f'Вы можете использовать программу ещё раз написав "python main.py" или перезапустив скрипт\n\nПрограмма написана программистом @Opasniy_chel (Telegram)')
        else:
            print(Fore.RED + f'Сайт не работает\n'
                  f'Код ошибки: {check_site.status_code}\n\nПрограмма написана программистом @Opasniy_chel (Telegram)')
    except:
        print('Неверно введён адрес')
# Пожалуйста не трогайте этот скрипт
# Программа написана программистом @Opasniy_chel (Telegram)