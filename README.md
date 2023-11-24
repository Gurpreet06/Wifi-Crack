## Acknowledgments
- Original Author: Gurpreet ~ Singh (@Gurpreet06) and the orginal 
- Updated by: Arkhalis (@Arkha1is) 

- The script is intended for use on Debian based systems, therefore compatibility with other systems is not officially supported or maintained.
- You can check your Network Interface by using the `ifconfig` command in the terminal.
- The script uses the rockyou wordlist for the Handshake attack by default.

# Wifi-Crack
WiFi-Crack is a Python tool designed to automate WiFi attacks in order to obtain a handshake, perform a PMKID attack, temporarily bring down networks through a denial-of-service (DOS) attack, create fake random access points, and launch an Evil Twin attack. This tool is useful for testing the security of wireless networks and can aid in the discovery of vulnerabilities in the network.

## The Wifi-Crack program has 6 attack modes.

#### Handshake attack
The Handshake attack mode allows you to obtain a valid handshake with which you can later apply a brute force attack to obtain the Wi-Fi password.

#### PKMID Attack
PKMID Attack mode is for wireless networks that do not have associated clients, and it tries to obtain a PMKID.

#### Authentication Denial-Of-Service
This Denial-of-Service-Mode starts as many requests as possible and keeps track of the 
answers, the AP sends using (MDK4). where mdk4 does itself keep track about clients, and 
even re-injects valid Data packets it intercepts from the network, so an AP may not be 
able to distinguish real and fake clients, and may start dropping legitimate ones to 
free up space.

#### Deauthentication attack
Deauthentication attack is used against wireless connections. It is like a denial-of-service, abruptly rendering
networks temporarily inactive. In this mode you can define the time until you want the attack to perform.

#### Beacon Flooding attack
In this attack scenario concerns the connectivity confusion of a wireless client. We are going to transmit countless 
fake beacon frames.

#### Evil Twin attack
In this evil twin attack we will set up a fake Wi-Fi access point hoping that users will connect to it instead of a 
legitimate one. When users connect to this access point, all the data they share with the network we will save it into
a file.

## Installations
First we install the necessary libraries to run this script correctly, with the following command.
```bash 

❯ pip3 install -r requirements.txt

```

## Original version tested on the following operating systems:
- Kali linux 2022.2
- Parrot security 5.0.1

#### Updated version personally tested by Arkhalis on the following operating system:
- Ubuntu 22.04

## Examples of How To Use
The program has 2 parameters:

The first parameter "-i" to specify the name of the network card (without monitor mode). The second parameter "-m" to specify the attack mode (Handshake | PKMID | AAuth | DAuth | BFlood | ETwin).

The program has a help menu with the "-h" parameter.

### Help Menu
```bash
❯ python3 wifiCrack.py

[!] Usage: sudo python3 wifiCrack.py -i <Network interface> -m <Attack mode>
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

┃  [-i] Network interface

┃  [-m] Attack mode
         Handshake (Capture a handshake)
         PKMID (Clientless attack)
         AAuth (Authentication Denial-Of-Service)
         DAuth (Deauthentication attack)
         BFlood (Beacon flooding attack)
         ETwin (Evil Twin attack)

┃  [-h] Help Panel
```

### Usage
```bash
❯ sudo python3 wifiCrack.py -i wlan0 -m handshake / PKMID / AAuth / DAuth / BFlood / ETwin
```

# Legal Notice

## Disclaimer
This script is provided for educational and informational purposes only. It is designed to promote understanding and knowledge of the subject matter. It is not intended to be used for illegal activities.

The author and contributors of this script do not condone, promote, or endorse any form of illegal and/or unethical activity. The use of this script for any illegal activities is strictly prohibited. 

The author and contributors of this script assumes no responsibility or liability for any misuse of this script, or for any damages that may arise, directly or indirectly, from such misuse. 

The use of this script is at your own risk. If you choose to use this script, you agree to accept all legal and ethical responsibility for your actions.

By using this script, you agree to this disclaimer and you waive any rights to hold the author of this script liable for any damage, harm, or legal issues caused by the misuse of this script.




Remember, hacking is illegal. If you engage in any illegal activity, you are responsible for your actions.
