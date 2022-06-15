"""This script generates the menu for the console application"""
from options.checkCorruptedInstall import compare_md5
from options.internetTest import print_results
from options.spaldotechServiceStatus import check_status
from options.testPermissions import test_permissions_in_dir
from options.clearScreen import clear_screen
from options.checkJava import determine_compatible_version
from options.play66 import order_66
from colorama import Fore, Back, Style
from welcome import back_to_menu, background_music, music_play, print_art
from time import sleep
from playsound import playsound
import os

menu_options = {
    1: "Test Internet Connectivity",
    2: "Check Spaldotech Service Status",
    3: "Test file permissions",
    4: "Verify Java Version",
    5: "Verify Modpack Installation",
    9: "Clear Terminal Window",
    0: "Exit"
}

def print_menu():
    for key in menu_options.keys():
        print (Fore.CYAN, key, Style.RESET_ALL, "--", menu_options[key] )

def menu_handler():
    while(True):
        back_to_menu()
        print_menu()
        print("\n")
        option = ''
        try:
            option = int(input(Fore.YELLOW + 'Enter menu option: ' + Style.RESET_ALL))
        except:
            print(Fore.RED + 'Error detecting option. Did you enter a number?' + Style.RESET_ALL)
        #Check what choice was entered and act accordingly
        if option == 1:
            print("\n")
            print_results()
        elif option == 2:
            print("\n")
            print_results()
            check_status()
        elif option == 3:
            print("\n")
            test_permissions_in_dir()
        elif option == 4: 
            print("\n")
            determine_compatible_version()
        elif option == 5:
            compare_md5()
        elif option == 9:
            clear_screen()
            print_art()
        elif option == 66:
            order_66()
            clear_screen()
            print_art()

        elif option == 0:
            print(Fore.GREEN + Style.BRIGHT + "Thank you for using this tool!" + Style.RESET_ALL)
            # playsound('assets/touche.mp3')
            sleep(2)
            quit()
        else:
            print(Fore.RED + 'Invalid option. Please enter a number between 1 and 6.' + Style.RESET_ALL)
            print("\n")
