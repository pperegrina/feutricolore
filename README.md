# feutricolore

## Intro

Project to control traffic lights from a Raspberry Pi with KS0212 keyestudio RPI 4-channel Relay Shield

See: https://wiki.keyestudio.com/index.php/KS0212_keyestudio_RPI_4-channel_Relay_Shield 

Be careful with GPIO pin numnbers, python wiringpi pin numbers are the real ones that can be found here: https://fr.pinout.xyz/pinout/wiringpi

Example: for wiringpi 3 used in KS0212 sample C code, we need to use 15 in python code.

## Installation

See: https://pimylifeup.com/raspberry-pi-django/

On Raspberry Pi, pi user:

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

sudo apt-get install git python3-venv
cd /home/pi/
git clone https://github.com/pperegrina/feutricolore.git
cd feutricolore
python3 -m venv djenv
source djenv/bin/activate
pip install -r requirements.txt

sudo mkdir /data
sudo chmod 777 /data
sudo vi /etc/rc.local

#!/bin/sh -e
#
# rc.local
#
# This script is executed at the end of each multiuser runlevel.
# Make sure that the script will "exit 0" on success or any other
# value on error.
#
# In order to enable or disable this script just change the execution
# bits.
#
# By default this script does nothing.

# Print the IP address
_IP=$(hostname -I) || true
if [ "$_IP" ]; then
  printf "My IP address is %s\n" "$_IP"
fi
/home/pi/feutricolore/feutricolore/start_server.sh
exit 0
```

Add rc.local service using this doc : https://www.troublenow.org/752/debian-10-add-rc-local/

## Screeshot

At boot, a server python script is started to control lights in the background.
A web page allows to change the sequence (using a file to send the info to the server script).
This is how it looks like
![alt text](https://github.com/pperegrina/feutricolore/raw/main/docs/Screenshot.png "Single page app")
