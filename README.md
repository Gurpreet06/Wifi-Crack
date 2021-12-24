# Wifi-Crack

## The Wifi-Crack program has 2 attack modes.

#### Handshake attack
The Handshake attack mode, where we can obtain a valid handshake with which later we can apply brute force attack to obtain the Wi-Fi password.

#### PKMID Attack
PKMID Attack mode which focuses its attention on wireless networks that do not have associated clients.


## Examples of How To Use
The program has 2 parameters, the first parameter "-n" to specify the name of the network card.
The second parameter '-a' to specify the attack mode (Handshake | PKMID).

The program also have a help menu with the parameter "-h"

```python
❯ sudo python3 wifiCrack.py

    [*] Usage: python3 main.py <Network InterFace> <parameters>
    -a  Attack mode
             Handshake
             PKMID (Not Working)
    -n Network card name
    -h Help Pan
```