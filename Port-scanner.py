import socket

def scan(target, ports):
    print('\n' + 'Starting scan for ' + str(target))
    for port in range(1, ports): 
        scan_port(target, port)
def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Port Open " + str(port))
        sock.close()
    except:
            print("[-] Port closed " + str(port))

target = input("[*] Enter targets to scan (split them by ,): ")
ports = int(input("[*] Enter how many ports you want to scan: "))
if ', ' in target:
    print("[*] Scanning Multiple Targets")
    for ip_addr in target.split(','):
        scan(ip_addr.strip(' '), ports)
else:
    scan(target,ports)

