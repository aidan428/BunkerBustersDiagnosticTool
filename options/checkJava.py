"""Determine Java Version installed"""
import os
import subprocess
from colorama import Fore, Back, Style
from time import sleep


modpack_compatible_java_version = 1.8

def print_env_variables():
    for k, v in os.environ.items():
        print(f'{k}={v}')

def get_java_home_version():
    java_home = os.environ['JAVA_HOME']
    #open release file and copy line one into string
    try:
        with open(java_home + "release") as f:
            firstline = f.readline().rstrip()
    except Exception as e:
        print(Fore.RED + "Unable to read releases file from JAVA_HOME" + Style.RESET_ALL)
        sleep(2)
        print(Fore.YELLOW + "Please navigate to " + java_home +" and determine the java version" + Style.RESET_ALL)
        exit()
    return firstline
    
def edit_string_version_str():
    java_version_float = float(get_java_home_version()[14:17])
    return java_version_float

def sub_menu_to_download_java_8():
    while True:
        print("Would you like to open a browser to download the supported Java version? (Y/N)")
        print("\n")
        option = ''
        try:
            option = input(Fore.YELLOW + 'Enter option: ' + Style.RESET_ALL)
        except:
            print(Fore.RED + 'Error detecting option. Did you enter Y or N?' + Style.RESET_ALL)
        if option == "Y" or option == "y":
            # Attempt to open edge in incognito mode and navigate to the link to download Quick Stego. Failing that produces a generic error and then the error trace.
            try:
                subprocess.call("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe --profile-directory=Default https://drive.google.com/file/d/1SaTnet-3K-9j5VqCxQS_qZckjgrmSYTp/view?usp=sharing")
                print(Fore.GREEN + "The browser has opened. Please download the exe file and install Java. This tool will now exit. \nGoodbye!")
                exit()
            except Exception as e:
                print(Fore.RED + "The default browser could not be opened. Please navigate to the following link: " + Style.RESET_ALL + "https://drive.google.com/file/d/1SaTnet-3K-9j5VqCxQS_qZckjgrmSYTp/view?usp=sharing")
                exit()
        elif option == "N" or option == "n":
                print(Fore.YELLOW + "Please navigate to the following link in your own time to download the correct version: " + Style.RESET_ALL + "https://drive.google.com/file/d/1SaTnet-3K-9j5VqCxQS_qZckjgrmSYTp/view?usp=sharing")
                sleep(2)
                print(Fore.GREEN + "Goodbye!")
                exit()
        else:
            print(Fore.RED + "Please don't be silly! That isn't Y or N." + Style.RESET_ALL)

                



def determine_compatible_version():
    if edit_string_version_str() == modpack_compatible_java_version:
        print(Fore.GREEN + "Java version compatible with Bunker Busters\n" + Style.RESET_ALL)
    elif edit_string_version_str() < modpack_compatible_java_version:
        print(Fore.RED + "Installed Java version is too old for Bunker Busters: Nuclear Rain")
        print(Fore.YELLOW + "Your version is " + str(edit_string_version_str()) + " whereas Bunker Busters requires version " + str(modpack_compatible_java_version) + Style.RESET_ALL + "\n")
        sub_menu_to_download_java_8()
    elif edit_string_version_str() > modpack_compatible_java_version:
        print(Fore.RED + "Installed Java version is too new for Bunker Busters: Nuclear Rain")
        print(Fore.YELLOW + "Your version is " + str(edit_string_version_str()) + " whereas Bunker Busters requires version " + str(modpack_compatible_java_version) + Style.RESET_ALL + "\n")
        sub_menu_to_download_java_8()
    else:
        print(Fore.RED + "An unknown error has occured!" + Style.RESET_ALL)


