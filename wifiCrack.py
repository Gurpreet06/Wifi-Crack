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
    if "macchanger" in check_macchanger.stdout:
        get_colours(f"\nMacchanger\t\t {Fore.GREEN + '(V)'}", "magenta")
    else:
        get_colours(f"\nMacchanger \t\t {Fore.RED + '(X)'}", "red")
        get_colours("Installing [Macchanger]....", "magenta")
        install_macchanger = subprocess.run(["sudo", "apt", "install", "macchanger", "-y"], capture_output=True,
                                            text=True)
        if "Setting up macchanger" in install_macchanger.stdout:
            get_colours("Macchanger Installed...", "blue")
    check_airmon_ng = subprocess.run(["which", "airmon-ng"], capture_output=True, text=True)
    if "airmon-ng" in check_airmon_ng.stdout:
        get_colours(f"\nAirmon-ng \t\t {Fore.GREEN + '(V)'}", "magenta")
    else:
        get_colours(f"\nAirmon-ng \t\t {Fore.RED + '(X)'}", "red")
        get_colours("\nInstalling [Airmon-ng]....", "magenta")
        install_airmon_ng = subprocess.run(["sudo", "apt", "install", "airmon-ng", "-y"], capture_output=True,
                                           text=True)
        if "Setting up airmon-ng" in install_airmon_ng.stdout:
            get_colours("Airmon-ng Installed...", "blue")

def attack_func(network_interface, attack_mode):
    print(" ")