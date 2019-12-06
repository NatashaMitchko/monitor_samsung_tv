# What is my tv doing?

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


Connected devices I know about:
- Phone
- Computer
- Work Phone
- Work Computer
- TV
- Google Home
