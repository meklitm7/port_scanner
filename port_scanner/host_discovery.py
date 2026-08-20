import ipaddress, subprocess, sys

ip_addr = sys.argv[1]
ip_class = sys.argv[2].upper()

try:

  ip = ipaddress.ip_address(ip_addr)

except:

  print("invalid ip")
  exit()

if ip_class == "A":

  network = ipaddress.ip_network(ip_addr + "/8", strict=False) 
  #strict=False use for calulate network add

elif ip_class == "B":

  network = ipaddress.ip_network(ip_addr + "/16", strict=False)

elif ip_class == "C":

  network = ipaddress.ip_network(ip_addr + "/24", strict=False)

else:

  print("invalid class")
  exit()

print("network address: ", network)
print("checking hosts...\n")

for host in network.hosts(): # get individual host

  result = subprocess.run(
    ["ping", "-c", "1", "-W", "1", str(host)],# it's like run ping -c 1 -W 1 ip
    stdout = subprocess.DEVNULL, # ping display a lot info so i hides by using this 
    stderr = subprocess.DEVNULL  # hides error output
  )

  if result.returncode == 0: # if returncode = 0 it is mean ping succeeded

    print(host, "up")

  else:

    print(host, "down")

