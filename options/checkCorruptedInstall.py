import hashlib
import sys
import requests
import json
from options.testPermissions import test_permissions_in_dir, check_default_dir_exists
from options.spaldotechServiceStatus import api_check, prepare_env
from time import sleep
from colorama import Fore, Back, Style

def get_forge_md5_from_api():
    response = requests.get(f"https://api.spaldotech.co.uk/api/mod/forge/1.12.2-14.23.5.2860")
    responseDict = json.loads(response.text)
    md5 = responseDict["md5"]
    return md5

def calculate_installed_forge_md5():
    userInstallDir = check_default_dir_exists()

    try:
        with open(userInstallDir + "\\cache\\forge-1.12.2-14.23.5.2860.zip", "rb") as user_forge_file:
            contents = user_forge_file.read()
            md5_returned = hashlib.md5(contents).hexdigest()
            return md5_returned
    except Exception as e:
        print(Fore.RED + "Unable to locate MD5. Please check your install directory is correct." + Style.RESET_ALL)
        # print(e)

def compare_md5():
    try:
        print(Fore.YELLOW + "Please stand by while the API is queried. Please note this can take a few moments." + Style.RESET_ALL )
        prepare_env()
        if api_check() == 1:
            if get_forge_md5_from_api() == calculate_installed_forge_md5():
                print(Fore.GREEN + "\nThe Forge Mod Loader version has passed MD5 verification and is not corrupted\n" + Style.RESET_ALL)
            else:
                print(Fore.RED + "The Forge Mod Loader version has failed to pass MD5 verification and may be corrupted\n" + Style.RESET_ALL)
                print(Fore.YELLOW + "Please select the 'reinstall pack' option from the modpack options section in the Technic Launcher. This will correct the Forge version.")
                sleep(4)
                print(Fore.GREEN + "This program will now exit")
                sys.exit(1)
        else:
            print(Fore.RED + "The API is not available. Please contact the system administrator!\n" + Style.RESET_ALL)

    except Exception as e:
        print(e)
