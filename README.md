# remotermin
it's a program to controle another laptop in the same network, whatever the os he uses :)

maybe to controle a raspberry from the command lines, or a phone from your laptop 

# HOW TO INSTALL IT

```sh
git clone https://github.com/NacreousDawn596/remotermin
cd remotermin
sudo apt-get install python3 python3-pip
pip3 install -r requirements.txt
```

# HOW TO USE IT

***for the device where the program gonna be hosted:***
```sh
python3 main.py
```

***for the devices that gonna be connected:***
```sh
#you should have the ip and the port of the other device
python3 connect.py 192.168.x.x:5000
```

*enjoy!*
