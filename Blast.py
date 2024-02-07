import sys,os
from colorama import Fore

print(Fore.MAGENTA+"""
 ___    _                 _       ___                                      _   
(  _`\ (_ )              ( )_    (  _`\                   _               ( )_ 
| (_) ) | |    _ _   ___ | ,_)   | |_) ) _ __    _       (_)   __     ___ | ,_)
|  _ <' | |  /'_` )/',__)| |     | ,__/'( '__) /'_`\     | | /'__`\ /'___)| |  
| (_) ) | | ( (_| |\__, \| |_    | |    | |   ( (_) )    | |(  ___/( (___ | |_ 
(____/'(___)`\__,_)(____/`\__)   (_)    (_)   `\___/' _  | |`\____)`\____)`\__)
                                                     ( )_| |                   
                                                     `\___/'                   
BY: S1riu_SS and SpyreX
""")

def display_menu():
    print(Fore.GREEN + """
    1: Blast-Tool (Hacking Tools)      | 2: Blast-Paid-Tools
    3: Info (about-us)
    """)

def execute_command(command):
    if command == '1':
        os.system('cmd /k "python Zero-Tool/zero-tool.py"' if os.name == 'nt' else 'python Zero-Tool/zero-tool.py')
    elif command == '2':
        print(Fore.RED + 'This option is not available yet! Coming soon...')
        #os.system('cmd /k "python Zero-Web-Hacktool/web_bugger.py"')
    elif command == '3':
        os.system('cmd /k "python info.py"' if os.name == 'nt' else 'python info.py')

        display_menu()
    else:
        print('Invalid option! Please choose the correct one.')

while True:
    display_menu()
    command = input('> ')

    if command.lower() == 'exit':
        break

    execute_command(command)
