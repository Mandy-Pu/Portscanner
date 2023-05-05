# Portscanner
A python script to identify open ports of a target device.

This script utilizes the python script library to identify open ports of a target device. The script works by establishing a connection with the target device using the socket.connect library function. If the connection is succesfully made then the port is classified as open.

Users can specify a single or multiple target IP addresses. Additionally, the number of ports to scan is required as well. The script always scans from the first port to the number specified by the user.

Run the script by typing "python3 portscanner.py" in the terminal. You will be prompted to input target IP addresses and the port range.
