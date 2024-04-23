# intervalometer
 
Code for raspberry pi based intervalometer for Nikon D90 Camera

Uses a very bad looking web UI and an ad hoc network to control intervalometer. Idk ill finish the readme when its done


# Prerequisits
install python

install django - https://docs.djangoproject.com/en/5.0/topics/install/ <--> sudo pip3 install django // Needs to be installed by root

install g++ - sudo apt-get install g++ //Should work

install pigpio - https://abyz.me.uk/rpi/pigpio/download.html

install ad hoc network - https://www.stevemurch.com/setting-up-a-raspberry-pi-for-ad-hoc-networking-tech-note/2022/12

- Makes sure to record your network ip
- would recommend to git clone this repo before adding the ad-hoc network, there are /wifi/.sh files for switching wifi to ad-hoc network, not hard, just need to copy some files

# How install
Do all of the prerequisits
clone this repo to the pi

move the /install/intervalometerpi.service to /etc/systemd/system/intervalometerpi.service

edit the file to change to the proper username //could make a new user if this is a shared system

edit intervalometerPi/intervalometerPi/settings.py and add your network ip (the ip of this pi) to the allowed host, should look something like this.
- ALLOWED_HOSTS = ["192.168.12.1"]
- ALLOWED_HOSTS = ["192.168.12.1","10.10.2.1"]

plug in the desired out pins of the pi, default is below. See hardware portion below for info
- camControl.cpp
- int shutter = 23;
- int focus = 24;
- If you want to change anything about that file make sure to re-complile it, the complile command is commented in the cpp
- Just make sure they are gpio pins if you change them

from there just start the service
- sudo systemctl status intervalometerpi //Shows the status of the the service
- sudo systemctl start intervalometerpi //Starts the service
- sudo systemctl enable intervalometerpi //Will have the system start the service when the pi boots, make sure to run

Connect to the hosted wifi on your phone and navicate to <your network ip>:8000

# Hardware





