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


def menu_panel():
    get_colours("[*] Usage: python3 main.py <Network InterFace> <parameters>", "green")
    get_colours("-a  Attack mode", "yellow")
    get_colours(f"\t Handshake", "yellow")
    get_colours(f"\t PKMID (Not Working)", "cyan")
    get_colours("-n Network card name", "yellow")
    get_colours("-h Help Panel", "yellow")


def check_deps():
    get_colours("\nChecking necessary programs...", "cyan")
    check_macchanger = subprocess.run(["which", "macchanger"], capture_output=True, text=True)
    