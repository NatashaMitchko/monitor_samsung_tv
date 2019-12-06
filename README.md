# What is my tv doing?

Rescources:
- https://lifehacker.com/know-your-network-the-complete-guide-5833254
- `brew install nmap`

Notes:

How are network packets constructed (http)?

https wrapped in an ip-packet (address and return address)
all that is wrapped in an ethernet frame

preamble + SFD (8 bytes)
destination address (6 bytes)
source address (6 bytes)
VLAN TAG (4 bytes)
Type/ Length (2 bytes)
Data/ Payload (42-1500 bytes)
Frame Check Sequence (CRC)

Naming your wireless network is really naming the service set identifier (SSID)
The name of your router is how it is identified to other devices on the network


Okay, found the samsung tv mac address...
`sudo nmap -sn X.X.X.X/24`

Connected devices I know about:
- Phone
- Computer
- Work Phone
- Work Computer
- TV
- Google Home

Next steps:
- script to monitor outbound traffic from the samsung tv mac address

