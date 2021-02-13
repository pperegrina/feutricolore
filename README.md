# feutricolore

## Intro

Project to control a traffic lights controller card with 2 buttons from a Raspberry Pi with KS0212 keyestudio RPI 4-channel Relay Shield

See:
- https://wiki.keyestudio.com/index.php/KS0212_keyestudio_RPI_4-channel_Relay_Shield
- https://www.deco-americaine.com/produit/sequenceur-dalternance-des-feux-tricolores-220v/

Be careful with GPIO pin numnbers, python wiringpi pin numbers are the real ones that can be found here: https://fr.pinout.xyz/pinout/wiringpi

Example: for wiringpi 3 used in KS0212 sample C code, we need to use 15 in python code.

## Installation

On Raspberry Pi (assuming installation for pi user, thanks to this doc : https://pimylifeup.com/raspberry-pi-django/)

```
sudo apt install apache2 -y
sudo apt install libapache2-mod-wsgi-py3
sudo vim /etc/apache2/sites-enabled/000-default.conf

<VirtualHost *:80>
	ServerAdmin webmaster@localhost
	DocumentRoot /home/pi/feutricolore/static
	ErrorLog ${APACHE_LOG_DIR}/error.log
	CustomLog ${APACHE_LOG_DIR}/access.log combined
  Alias /static /home/pi/feutricolore/static
  <Directory /home/pi/feutricolore/static>
      Require all granted
  </Directory>
  <Directory /home/pi/feutricolore/feutricolore>
      <Files wsgi.py>
          Require all granted
      </Files>
  </Directory>
  WSGIDaemonProcess django python-path=/home/pi/feutricolore python-home=/home/pi/feutricolore/djenv
  WSGIProcessGroup django
  WSGIScriptAlias / /home/pi/feutricolore/feutricolore/wsgi.py
</VirtualHost>

sudo systemctl restart apache2
sudo usermod -a -G gpio www-data
cd /home/pi/
git clone git@github.com:/pperegrina/feutricolore
cd feutricolore
python3 -m venv djenv
source djenv/bin/activate
pip install -r requirements.txt
```

## Screeshot

This is how it looks, clicking on a sequence will send the right buttons sequence on traffic light controller to set it

![alt text](https://github.com/pperegrina/feutricolore/raw/main/doc/Screenshot.png "Single page app")
