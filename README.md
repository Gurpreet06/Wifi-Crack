# Wifi-Crack

## The Wifi-Crack program has 4 attack modes.

#### Handshake attack
The Handshake attack mode, where we can obtain a valid handshake with which later we can apply brute force attack to obtain the Wi-Fi password.

#### PKMID Attack
PKMID Attack mode is for wireless networks that do not have associated clients, and it tries to obtain a PMKID.

#### Deauthentication attack
Deauthentication attack is used against wireless connections. It is like a denial-of-service, abruptly rendering
networks temporarily inactive. In this mode you can define the time until you want the attack to perform.

#### Beacon Flooding attack
In this attack scenario concerns the connectivity confusion of a wireless client. We are going to transmit countless 
fake beacon frames.

## Installations
First we install the necessary libraries to run this script correctly, with the following command.
```bash 

❯ pip3 install -r requirements.txt

```

## Tested on the following operating systems:
- Kali linux 2022.1
- Parrot security 4.11.3

## Examples of How To Use
The program has 2 parameters, the first parameter "-n" to specify the name of the network card.
The second parameter '-a' to specify the attack mode (Handshake | PKMID | DAuth | BFlood).

The program also has a help menu with the parameter "-h"

### Help Menu
```bash
❯ python3 wifiCrack.py

[!] Usage: sudo python3 wifiCrack.py -n <Network InterFace> -a <parameters>
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

┃  [-n] Interface in monitor mode

┃  [-a] Attack mode
         Handshake
         PKMID
         DAuth (Deauthentication attack)
         BFlood (Beacon flooding attack)

┃  [-h] Help Panel
```

### Usage
```bash
❯ sudo python3 wifiCrack.py -n wlan0 -a handshake / PKMID / DAuth / BFlood
```

# Legal Notice

This script is intended to be used on networks you own. Don't use this script maliciously. You are responsible for your own actions.
