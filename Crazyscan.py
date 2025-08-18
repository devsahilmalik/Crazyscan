import argparse
import socket
parser = argparse.ArgumentParser(description="the network scanner")
parser.add_argument("-i", "--ip", help="target ip address")
parser.add_argument("-p", "--port", help="specific ports")
parser.add_argument("-t", "--timeout", default=0.5, type=float, help="timeout")
parser.add_argument("-v", "--version", action="store_true", help="version")
args = parser.parse_args()
if args.port:
	ports_list = [int(p.strip()) for p in args.port.split(",") if p.strip().isdigit()]
else:
	ports_list = [80,23,443,21,22,25,3389,110,445,139,143,53,135,3306,8080,1723,111,995,993,5900,1025,587,8888,199,1720,465,546,113,81,6001,514,5060,179,1521,1433,4662,554,8081,32768,6667,8000,2049,7070,4444,2000,6000,9090,10000,2048]
def scanner(ip, ports, timeout):
	print(f"scanning on target ip address {ip}")
	for port in ports:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(timeout)
		result = s.connect_ex((ip, port))
		if result == 0:
			print(f"[+] port {port} is open")
		s.close()
if args.version:
	print("Crazyscan version 1.0")
elif args.ip:
	scanner(args.ip, ports_list, args.timeout)
else:
	print("the following arguments are required -i/ --ip(unless using -v)")