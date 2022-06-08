"""File to test the file permissions in BB directory"""

from colorama import Fore, Back, Style
from genericpath import isdir
from time import sleep
import os
import sys


def check_default_dir_exists():
    path = "C:\\Users\\" + get_username() + "\\AppData\\Roaming\\.technic\\modpacks\\bunkerbusters-nuclear-rain\\bin"
    isdir = os.path.isdir(path)

    if isdir == True:
        print(Fore.GREEN + "Bunker Busters: Nuclear Rain directory located!" + Style.RESET_ALL)
        return path
    else:
        print(Fore.RED + "Bunker Busters: Nuclear Rain is not installed to the default directory" + Style.RESET_ALL)
        userLocation = str(input(Fore.YELLOW + 'Please enter the Bunker Busters install location : ' + Style.RESET_ALL))
        BBUserDir = userLocation + "\\bin"
        userCheck = os.path.isdir(BBUserDir)
        # print("DEBUG: " + BBUserDir + "   true")

        if userCheck == True:
            print(Fore.GREEN + "Bunker Busters: Nuclear Rain directory located!" + Style.RESET_ALL)
            return BBUserDir
        else:
            print(Fore.RED + "Failed to locate directory. Please locate the directory and re-run this tool." + Style.RESET_ALL)
            sys.exit(0)
            

def get_username():
    username = os.getlogin()
    return username

def test_permissions_in_dir():
    base_dir = check_default_dir_exists()

    try:
        f = open(base_dir + "permissionsTest.txt", "a")
        f.write("Permissions test pass")
        f.close()
        print(Fore.GREEN + "Bunker Busters: Nuclear Rain directory has read and write permissions!" + Style.RESET_ALL)
        print("\n")
    except Exception as e:
        print(Fore.RED + "The Bunker Busters: Nuclear Rain base directory is not writable." + Style.RESET_ALL)
        sleep(2)
        print(Back.YELLOW + "Please reinstall the Technic Launcher from TechnicPack.net and select a new directory during the setup" + Style.RESET_ALL)


    

