import requests
import colorama
import sys, os
import time
colorama.init(autoreset=True)
#Continung l8ter
session = requests.Session()

beginning = colorama.Fore.GREEN + """

  /$$$$$$                   /$$           /$$                   /$$/$$      /$$                  /$$      /$$
 /$$__  $$                 |__/          | $$                  | $| $$  /$ | $$                 | $$     | $$
| $$  \__/ /$$$$$$$ /$$$$$$ /$$ /$$$$$$ /$$$$$$   /$$$$$$  /$$$$$$| $$ /$$$| $$ /$$$$$$  /$$$$$$| $$ /$$$$$$$
|  $$$$$$ /$$_____//$$__  $| $$/$$__  $|_  $$_/  /$$__  $$/$$__  $| $$/$$ $$ $$/$$__  $$/$$__  $| $$/$$__  $$
 \____  $| $$     | $$  \__| $| $$  \ $$ | $$   | $$$$$$$| $$  | $| $$$$_  $$$| $$  \ $| $$  \__| $| $$  | $$
 /$$  \ $| $$     | $$     | $| $$  | $$ | $$ /$| $$_____| $$  | $| $$$/ \  $$| $$  | $| $$     | $| $$  | $$
|  $$$$$$|  $$$$$$| $$     | $| $$$$$$$/ |  $$$$|  $$$$$$|  $$$$$$| $$/   \  $|  $$$$$$| $$     | $|  $$$$$$$
 \______/ \_______|__/     |__| $$____/   \___/  \_______/\_______|__/     \__/\______/|__/     |__/\_______/
                              | $$                                                                           
                              | $$                                                                           
                              |__/                         

ROBLOX multitool

"""

print(beginning)

def check_cookie():
    def delete_line():
        data = open(os.path.join(sys.path[0], "cookies.txt"), "r").read().splitlines(True)
        open(os.path.join(sys.path[0], "cookies.txt"), "w").writelines(data[1:])

    while os.stat(os.path.join(sys.path[0], "cookies.txt")).st_size != 0:
        time.sleep(0.2)
        headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
        }
        session.headers = headers
        cookie = str(open(os.path.join(sys.path[0], "cookies.txt"), "r").readline())
        session.cookies['.ROBLOSECURITY'] = cookie
        try:
            r = session.post('https://www.roblox.com/api/item.ashx?=cool')
        except ValueError:
            print(colorama.Fore.RED + 'Invaild Cookie')
            delete_line()
            check_cookie()
        session.headers['X-CSRF-TOKEN'] = r.headers['X-CSRF-TOKEN']
        r = session.get('https://api.roblox.com/currency/balance').json()
        try:
            if r['errors']:
                print(colorama.Fore.RED + ('Not working'))
                delete_line()
        except KeyError:
            print(colorama.Fore.GREEN + 'Working')
            open(os.path.join(sys.path[0], "working.txt"), "a").write('\n' + cookie + ' | Checked with ScriptedWorlds multitool')
            delete_line()
            if os.stat(os.path.join(sys.path[0], "cookies.txt")).st_size == 0:
                menu()

def menu():
    choice = input('1) Cookie Checker\nSelect: \n')
    if choice == '1':
        check_cookie()


def exit():
    input('Press any Key to exit')

menu()