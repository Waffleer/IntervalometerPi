# intervalometer
 
Code for raspberry pi based intervalometer for Nikon D90 Camera

Uses a very bad looking web UI and an ad hoc network to control intervalometer. Idk ill finish the readme when its done


# Prerequisits
install python

install django - https://docs.djangoproject.com/en/5.0/topics/install/ <--> sudo pip3 install django // Needs to be installed by root

install g++ - sudo apt-get install g++ //Should work

install pigpio - https://abyz.me.uk/rpi/pigpio/download.html

install ad hoc network - https://www.stevemurch.com/setting-up-a-raspberry-pi-for-ad-hoc-networking-tech-note/2022/12

# How to Run
sudo ./run.sh   //Has to be sudo, need perms for triggering the camera
