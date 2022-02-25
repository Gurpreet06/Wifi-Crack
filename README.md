# Wifi-Crack

## The Wifi-Crack program has 2 attack modes.

#### Handshake attack
The Handshake attack mode, where we can obtain a valid handshake with which later we can apply brute force attack to obtain the Wi-Fi password.

#### PKMID Attack
PKMID Attack mode is for wireless networks that do not have associated clients, and it tries to obtain a PMKID.


## Examples of How To Use
The program has 2 parameters, the first parameter "-n" to specify the name of the network card.
The second parameter '-a' to specify the attack mode (Handshake | PKMID).

The program also has a help menu with the parameter "-h"

### Help Menu
```bash
❯ sudo python3 wifiCrack.py -h

    [*] Usage: sudo python3 wifiCrack.py -n <Network InterFace> -a <parameters>
    -n Network card name
    -a  Attack mode
             Handshake
             PKMID
             DAuth
    -h Help Panel
```

### Usage
```bash
❯ sudo python3 wifiCrack.py -n wlan0 -a handshake / PKMID
```
