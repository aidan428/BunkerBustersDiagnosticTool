"""This script generates the menu for the console application"""
from options.internetTest import print_results
from options.spaldotechServiceStatus import check_status
from options.testPermissions import test_permissions_in_dir
from options.clearScreen import clear_screen
from colorama import Fore, Back, Style
from welcome import background_music, music_play
from time import sleep
from playsound import playsound
import os

menu_options = {
    1: "Test internet connectivity",
    2: "Check Spaldotech service status",
    3: "Test file permissions",
    4: "Check Java version",
    5: "Check for corrupted install",
    9: "Clear Terminal Window",
    0: "Exit"
}

def print_menu():
    for key in menu_options.keys():
        print (key, "--", menu_options[key] )

def menu_handler():
    while(True):
        print_menu()
        print("\n")
        option = ''
        try:
            option = int(input(Fore.YELLOW + 'Enter menu option: ' + Style.RESET_ALL))
        except:
            print(Fore.RED + 'Error detecting option. Did you enter a number?' + Style.RESET_ALL)
        #Check what choice was entered and act accordingly
        if option == 1:
           print_results()
        elif option == 2:
            check_status()
        elif option == 3:
            test_permissions_in_dir()
        elif option == 9:
            clear_screen()
        elif option == 0:
            print(Fore.GREEN + Style.BRIGHT + "Thank you for using this tool!" + Style.RESET_ALL)
            # playsound('assets/touche.mp3')
            sleep(2)
            quit()
            

        else:
            print(Fore.RED + 'Invalid option. Please enter a number between 1 and 6.' + Style.RESET_ALL)
