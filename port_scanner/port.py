import socket, ipaddress, threading
from queue import Queue


ip_addr = input("enter your ip: ")

try:

  ip = ipaddress.ip_address(ip_addr)

except ValueError:

  print("invalid ip")
  exit()

protocol = input("""
1) TCP scan
2) UDP scan
Choose scanning type: """)

print("scanning in progress...")

def tcp_scanner(port):

  try:
      sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

      sock.connect((ip_addr, port))

      sock.close()

      return True

  except :
      
      return False

def udp_scanner(port):

  try:

      sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

      sock.settimeout(1)

      sock.sendto(b"hello", (ip_addr, port))

      data, address = sock.recvfrom(1024)

      sock.close()

      return True

  except socket.timeout:

      sock.close()

      return False

  except Exception:

      sock.close()

      return False

'''
 i used threads to speed up port scanning 
 i use a queue to prevent the same port from being checked twice
'''

queue = Queue()   # this is empty queue

open_port =[]

def fill_queue(port_list):

  for port in port_list:

    queue.put(port) # add the value into queue

def worker(): 
# this function for thread

  while not queue.empty():

    port = queue.get() # set next value of queue

    if protocol == "1":

      if tcp_scanner(port):

        print(f" TCP {port} is open")

        open_port.append(port)
    elif protocol == "2":

       if udp_scanner(port):

          print(f"UDP {port} is open")

          open_port.append(port)

    # we can also use else statement for closed ports but it would make the output too verbose

port_list = range(1,1025)

fill_queue(port_list) # fill the queue with ports from 1-1024

thread_list = [] #this created specifically for final line for loop without this list they won't work

for t in range(10 ): 

# 10 is number of thread if u increase the number of thread makes the port scanning faster

  thread = threading.Thread(target=worker) 

#i am refering to the worker function without actually calling

  thread_list.append(thread) # creat thread

for thread in thread_list:

  thread.start() # run all thread

for thread in thread_list:

  thread.join() # wait until all threads are finished 

print("open ports are ", open_port)









 