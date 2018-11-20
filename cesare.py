options = 0
list = []

while True:
    options = int(input("1 för att kryptera\n2 för att dekryptera\n3 för att avsluta\n"))
    if options == 1:
        list = []
        msg = input("skriv ditt meddelande du vill ha krypterat: ")
        key = int(input("skriv in din nyckel: "))
        for l in msg:
            qe = ord(l) + key    
            list += chr(qe)
        print(list)
    elif options == 2:
        if len(list) > 0:
            list2 = []
            for l in list:
                qe = ord(l) - key
                list2 += chr(qe)
            print(str(list2))
        else:
            print("Du har inget krypterat meddelande:")
    elif options == 3:
        break