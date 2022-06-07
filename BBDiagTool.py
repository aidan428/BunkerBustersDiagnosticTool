import welcome
from generateMenu import menu_handler
from colorama import init


def main():
    init() #used for the colours
    menu_handler()

# Standard boilerplate code to call the main() function to begin
# the program if run as a script.
if __name__ == '__main__':
    main()