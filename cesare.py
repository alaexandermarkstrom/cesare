msg = input("skriv ditt meddelande du vill ha krypterat:")
key = int(input("skriv in din nyckel:"))
list = []
for l in msg:
    list += chr(ord(l) + key)
print(list)