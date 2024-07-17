import socket
import termcolor
from concurrent.futures import ThreadPoolExecutor

def scan(target, ports):
    print(f'\nStarting Scan For {target} for {ports} ports.')
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(1, ports + 1):
            executor.submit(scan_port, target, port)

def scan_port(ipaddress, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            sock.connect((ipaddress, port))
            print(termcolor.colored(f"[+] Port Opened: {port}", 'green'))
    except:
        pass

def main():
    targets = input("[*] Enter Targets To Scan (split them by ,): ")
    ports = int(input("[*] Enter How Many Ports You Want To Scan: "))
    if ',' in targets:
        print(termcolor.colored("[*] Scanning Multiple Targets", 'green'))
        for ip_addr in targets.split(','):
            scan(ip_addr.strip(), ports)
    else:
        scan(targets, ports)

if __name__ == "__main__":
    main()