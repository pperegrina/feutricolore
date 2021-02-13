# feutricolore

Project to control a traffic lights controller card with 2 buttons from a Raspberry Pi with KS0212 keyestudio RPI 4-channel Relay Shield

See:
- https://wiki.keyestudio.com/index.php/KS0212_keyestudio_RPI_4-channel_Relay_Shield
- https://www.deco-americaine.com/produit/sequenceur-dalternance-des-feux-tricolores-220v/

Careful with GPIO pin numnbers, python wiringpi pin numbers are the real ones that can be found here: https://fr.pinout.xyz/pinout/wiringpi
Example: for wiringpi 3 used in KS0212 sample C code, we need to use 15 in python code.



