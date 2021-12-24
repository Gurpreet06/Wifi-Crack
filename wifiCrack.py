import sys
import os
import subprocess
import time
import signal
from colorama import Fore


# Colours
def get_colours(text, color):
    if color == "green":
        green_color = Fore.GREEN + text
        print(green_color)
    elif color == "red":
        red_color = Fore.RED + text
        print(red_color)
    elif color == "blue":
        blue_color = Fore.BLUE + text
        print(blue_color)
    elif color == "yellow":
        yellow_color = Fore.YELLOW + text
        print(yellow_color)
    elif color == "magenta":
        magenta_color = Fore.MAGENTA + text
        print(magenta_color)
    elif color == "cyan":
        cyan_color = Fore.CYAN + text
        print(cyan_color)

