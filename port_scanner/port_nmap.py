import nmap, ipaddress

scanner = nmap.PortScanner()

ip_addr = input("enter your ip address: ")

try:
    ipaddress.ip_address(ip_addr) # check if it is ip add or not
except ValueError:
    print("Invalid IP address")
    exit()

choice = input("""
                    1) stealth scan
                    2) tcp scan
                    3) udp scan
                    4) xmass scan
                  choose ur scanning type: """)
print("scanning in progress...")

def open_ports():
# this function do check if it is any protocol(udp,tcp) and check if it's open or not
  for protocol in scanner[ip_addr].all_protocols():
    print("Open ports:", scanner[ip_addr][protocol].keys()) #tell us if it is open or not


if choice == "1":

  scanner.scan(ip_addr,'1-1024', '-v -sS')

  print(scanner.scaninfo()) # give us info about the scanning process

  print("ip status: ", scanner[ip_addr].state()) # tell us if it is up or down

  print(scanner[ip_addr].all_protocols())

  open_ports()

elif choice == "2":

  scanner.scan(ip_addr,'1-1024', '-v -sT')

  print(scanner.scaninfo())

  print("ip status: ", scanner[ip_addr].state())

  print(scanner[ip_addr].all_protocols())

  open_ports()

elif choice == "3":

  scanner.scan(ip_addr,'1-1024', '-v -sU')

  print(scanner.scaninfo())

  print("ip status: ", scanner[ip_addr].state())

  print(scanner[ip_addr].all_protocols())

  open_ports()

elif choice == "4":

  scanner.scan(ip_addr,'1-1024', '-v -sX')

  print(scanner.scaninfo())

  print("ip status: ", scanner[ip_addr].state())

  print(scanner[ip_addr].all_protocols())

  open_ports()

else:

  print("your choice must be 1 to 4")


 