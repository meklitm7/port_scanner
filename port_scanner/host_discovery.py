import ipaddress

try:

    target = input("enter your ip: ")

    ip = ipaddress.ip_address(target)
    first = int(target.split(".")[0])

    if first >= 0 and first <= 127:

      print("Class A")

      if target == "1.0.0.1":

        print("this is getway ip")

    elif first >= 128 and first <= 191:

      print("Class B")

      if target == "128.0.0.1":

        print("this is getway ip")

    elif first >= 192 and first <= 223 :

      print("Class C")

      if target == "192.0.0.1":
      
          print("this is getway ip")

    elif first >= 224 and first <= 239 :

      print("Class D")

      if target == "224.0.0.1":
      
          print("this is getway ip")

    else:

      print("Class E")

      if target == "240.0.0.1":
      
          print("this is getway ip")

except ValueError :

   print("enter only a ip ")




