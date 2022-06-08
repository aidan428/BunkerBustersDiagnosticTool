from concurrent.futures import thread
from colorama import Fore, Back, Style
import click
from playsound import playsound
from threading import Thread


art = ''' ______     ______   ______     __         _____     ______     ______   ______     ______     __  __    
/\  ___\   /\  == \ /\  __ \   /\ \       /\  __-.  /\  __ \   /\__  _\ /\  ___\   /\  ___\   /\ \_\ \   
\ \___  \  \ \  _-/ \ \  __ \  \ \ \____  \ \ \/\ \ \ \ \/\ \  \/_/\ \/ \ \  __\   \ \ \____  \ \  __ \  
 \/\_____\  \ \_\    \ \_\ \_\  \ \_____\  \ \____-  \ \_____\    \ \_\  \ \_____\  \ \_____\  \ \_\ \_\ 
  \/_____/   \/_/     \/_/\/_/   \/_____/   \/____/   \/_____/     \/_/   \/_____/   \/_____/   \/_/\/_/ 
                                                                                                         '''

def generate_welcome() :
  print(art)
  print(Back.GREEN + "Welcome to the Bunker Busters: Nuclear Rain Diagnostic Tool v0.3" + Style.RESET_ALL)
  print(Fore.YELLOW + "Simply choose an option below by typing the menu number and pressing enter." + Style.RESET_ALL)
  print("\n")

def clear_screen():
  click.clear()

def music_play():
  playsound('assets/welcome.mp3')

def background_music():
  music_thread = Thread(target=music_play)
  music_thread.start()
  music_thread

clear_screen()
generate_welcome()
background_music()

