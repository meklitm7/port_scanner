import socket

target = input("enter your ip: ")

def portscanner(port):

  try:

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect((target,port))

    return True

  except Exception as e:

    print(e)

    return False


for port in range(1,1024):

  result = portscanner(port)

  if result:

    print(f"port {port} is open")

  else:

    print(f"port {port} is close")