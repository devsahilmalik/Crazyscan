import argparse
import socket
from concurrent.futures import ThreadPoolExecutor


parser = argparse.ArgumentParser(description="Fast network scanner")
parser.add_argument("-i", "--ip", help="Target ip address")
parser.add_argument("-p", "--ports", nargs="+", help="Specefic ports")
parser.add_argument("-t", "--timeout", default=0.5, type=float, help="Timeout")
parser.add_argument("-o", "--output", nargs="?", const="output.txt", help="save output")
parser.add_argument("-v", "--version", action="store_true", help="current version")
parser.add_argument("-th", "--threads", default=10, type=int, help="threads")
args = parser.parse_args()
count = 0
ports = []
if args.ports:
  ports = [int(p.strip()) for p in args.ports  if p.strip().isdigit()]
else:
  ports = [80,23,443,21,22,25,3389,110,445,139,143,53,135,3306,8080,1723,111,995,993,5900,1025,587,8888,199,1720,465,546,113,81,6001,514,5060,179,1521,1433,4662,554,8081,32768,6667,8000,2049,7070,4444,2000,6000,9090,10000,2048,]
output = ""
if args.output and args.output.endswith (".txt"):
  output = args.output
elif args.output and args.output.endswith("."):
  output = args.output + "txt"
elif args.output and args.output.endswith("txt"):
  output = (args.output[:-3]) + ".txt"
elif args.output:
  output = args.output + ".txt"
else:
  output = None
def scan_ports(ip, port, timeout):
  global output
  global count
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    s.connect((ip, port))
    result = (f"[+] Port {port} is open")
    print(result)
    count += 1
    if output:
      with open (output, "a") as f:
        f.write(result + "\n")
    s.close()
  except:
    pass
    
  
  


def threads_maker(ip, ports, timeout, threads):
  with ThreadPoolExecutor(max_workers=threads) as executor:
    for port in ports:
      executor.submit(scan_ports, ip, port, timeout)

def banner():
    print(r"""
:'######::'########:::::'###::::'########:'##:::'##:
'##... ##: ##.... ##:::'## ##:::..... ##::. ##:'##::
 ##:::..:: ##:::: ##::'##:. ##:::::: ##::::. ####:::
 ##::::::: ########::'##:::. ##:::: ##::::::. ##::::
 ##::::::: ##.. ##::: #########::: ##:::::::: ##::::
 ##::: ##: ##::. ##:: ##.... ##:: ##::::::::: ##::::
. ######:: ##:::. ##: ##:::: ##: ########:::: ##::::
:......:::..:::::..::..:::::..::........:::::..:::::
:'######:::'######:::::'###::::'##::: ##:           
'##... ##:'##... ##:::'## ##::: ###:: ##:           
 ##:::..:: ##:::..:::'##:. ##:: ####: ##:           
. ######:: ##:::::::'##:::. ##: ## ## ##:           
:..... ##: ##::::::: #########: ##. ####:           
'##::: ##: ##::: ##: ##.... ##: ##:. ###:           
. ######::. ######:: ##:::: ##: ##::. ##:           
:......::::......:::..:::::..::..::::..::

     C R A Z Y S C A N    |  Free Pelestine
     Author sahil         - 
..............................................
..............................................""")
        






if args.version:
  print("Crazyscan version 1.2")
elif args.ip:
  banner()
  print(f"Scanning on target ip {args.ip}")
  threads_maker(args.ip, ports, args.timeout, args.threads)
  if count == 0:
    if args.ports:
      for p in args.ports:
        print(f"port {p} is not open")
    else:
      print("No port is open")
else:
  print("type Crazyscan -h for help and usage")