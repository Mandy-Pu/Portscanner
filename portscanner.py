import socket
# printing statements in different colors
import termcolor

def scan(target, ports):
	print(termcolor.colored(("\n" + "Starting scan for " + str(target)), "blue"))
	for port in range(1, ports):
		scan_port(target, port)


def scan_port(ipaddress, port):

	try:
		sock = socket.socket()
		sock.connect((ipaddress, port))
		sock.close()
		print(termcolor.colored(("[+] " + str(port) + " is open"), "green"))
	except:
		pass

targets = input("[*] Enter targets to scan(split targets by ,): ")
ports =int(input("[*] Enter ports to scan: "))

if "," in targets:
	print(termcolor.colored(("[*] Scanning multiple targets"), "blue"))
	for target in targets.split(","):
		scan(target.strip(" "), ports)
else:
	scan(targets, ports)



