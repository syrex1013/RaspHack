# RaspHack
Simple raspberry hacking program.

Script tries to find raspberry pi's using shodan and then tries to login to them using **pi:raspberry**  

# Requirements
    Paramiko
    Shodan
    colorama
# How to (shodan version)
    raspberry-hacker.py -k <SHODAN KEY>
  Program will start searching for raspberry pi's and then it tries to connect to it.
# How to (single host version)
    raspberry-hacker.py -k <Shodan key> -a <ip address> -l <login> -p <password>
      
