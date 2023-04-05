f = open ("logo.bmp", 'rb')
f.seek(0)
bytes = f.read(16)
f.close
length = len(bytes)
print(bytes[9:11])
print(length)
print(f.tell())
