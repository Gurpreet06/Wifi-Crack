# Wifi-Crack
WiFi-Crack is a Python tool designed to automate WiFi attacks in order to obtain a handshake, perform a PMKID attack, temporarily bring down networks through a denial-of-service (DOS) attack, create fake random access points, and launch an Evil Twin attack. This tool is useful for testing the security of wireless networks and can aid in the discovery of vulnerabilities in the network.

## The Wifi-Crack program has 6 attack modes.

#### Handshake attack
The Handshake attack mode, where we can obtain a valid handshake with which later we can apply brute force attack to obtain the Wi-Fi password.

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

## Tested on the following operating systems:
- Kali linux 2022.2
- Parrot security 5.0.1

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

This script is intended to be used on networks you own. Don't use this script maliciously. You are responsible for your own actions.
