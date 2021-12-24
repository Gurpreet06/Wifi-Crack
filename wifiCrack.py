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
    get_colours("[*] Usage: sudo python3 wifiCrack.py <Network InterFace> <parameters>", "green")
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
    time.sleep(1)
    subprocess.run(["clear"])
    get_colours("\nSetting up network card...", "yellow")
    subprocess.run(["sudo", "airmon-ng", "start", network_interface])
    get_colours("\nGetting new Mac Address...", "yellow")
    time.sleep(3)
    subprocess.run(["sudo", "ifconfig", network_interface + "mon", "down"])
    subprocess.run(["sudo", "macchanger", "-r", network_interface + "mon"])
    subprocess.run(["sudo", "ifconfig", network_interface + "mon", "up"])
    get_colours("\n New Mac Address Generated ", "blue")
    time.sleep(1)
    subprocess.run(["clear"])
    
    # HandShake Attack Mode
    if attack_mode == "Handshake":
        os.system(f"xterm -hold -e sudo airodump-ng {network_interface}mon &")



def stop_attack(network_interface, attack_parm):
    if attack_parm == "STOP":
        get_colours("Stoping attack...", "red")
        subprocess.run(["sudo", "airmon-ng", "stop", network_interface + "mon"])
        get_colours("Network set to it's normal mode...", "magenta")
        get_colours("[*] Exiting the program...", "blue")


def ctrl_c(signum, frame):
    subprocess.run(["sudo", "airmon-ng", "stop", "wlan0mon"])
    get_colours("[*] Exiting the program...", "blue")
    exit(1)


def check_parms():
    if len(sys.argv) > 1:
        if sys.argv[1] == "-h":
            menu_panel()
        elif len(sys.argv) > 2:
            if len(sys.argv) > 3:
                if len(sys.argv) > 4:
                    check_interface_exist = subprocess.run(["ifconfig"], capture_output=True, text=True)
                    check_attack_mode = ["Handshake", "PKMID"]
                    if sys.argv[2] not in check_interface_exist.stdout:
                        get_colours("Select a valid Interface..", "red")
                    elif sys.argv[4] not in check_attack_mode:
                        get_colours("Select a valid attack Mode..", "red")
                    else:
                        check_deps()
                        attack_func(sys.argv[2], sys.argv[4])
                else:
                    get_colours("Select a attack Mode..", "red")
            else:
                get_colours("Select a attack Mode..", "red")
        else:
            get_colours("\nIncorrect Option...", "red")
    else:
        menu_panel()


signal.signal(signal.SIGINT, ctrl_c)