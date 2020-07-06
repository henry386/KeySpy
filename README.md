# KeySpy
Key Logger in python than sends all data to an external server

## Usage:
1. Run the server.py code on the Host machine
2. Compile the client.py to an exe and remember to change the bool "Compiled" to true, this enbles persistance
3. Deploy to client by running it on the target device
4. You should now see on the host that a new client has connected, all the keys that user presses will appear on the server terminal screen as well as being saved to messagelog.txt in the directory of the host script.

## Issues
- May need you to bypass targets firewall on port 9989
- Close ALL services using port 9989 or change that port
