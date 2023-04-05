import struct

def size_checker (data):
    with open (data, 'rb') as f:
        #f.seek(0)
        BMP_signature = f.read(2)
        if BMP_signature == b'BM': #Why can't I treat it as a string?
            print("This is a legit BMP file.")
            f.seek(18) #File pointer to byte 18 to read width info.
            BMP_width = f.read(4)
            print(BMP_width)
            f.seek(22) #File pointer to byte 22 to read height info.
            BMP_height = f.read(4)
            print(BMP_height)
            print("Width (px):",struct.unpack('<L',BMP_width)[0])
            print("Height (px):",struct.unpack('<L',BMP_height)[0])
            return (BMP_width,BMP_height)
            #int_width = int.from_bytes(BMP_width, "little") #This was my initial approach!
            #int_height = int.from_bytes(BMP_height,"little")
            #print("Width (px)", int_width)
            #print("Height (px)", int_height)
        else :
            raise RuntimeError ("File has no valid signature")
            #print("This is not a BMP file.")
        

size_checker("logo.bmp")