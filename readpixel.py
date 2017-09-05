def bytes_to_i(mbytes, byteorder='little'):
    return int.from_bytes(mbytes, byteorder)

def i_to_bytes(number, length, byteorder='little'):
    return number.to_bytes(length, byteorder)

def readpixelfunction(image):
    file = open(image, "rb")

    #BmpFileHeader
    bfType = bytes_to_i(file.read(2))
    bfSize =  bytes_to_i(file.read(4))
    bfReserved1 =  bytes_to_i(file.read(2))
    bfReserved2 =  bytes_to_i(file.read(2))
    bfOffBits =  bytes_to_i(file.read(4))

    # BmpStructHeader
    biSize = bytes_to_i(file.read(4))
    biWidth =  bytes_to_i(file.read(4))        #picture width
    biHeight =  bytes_to_i(file.read(4))    #picture height
    biPlanes =  bytes_to_i(file.read(2))    #default 1
    biBitCount =  bytes_to_i(file.read(2))      #one pixel occupy how many bits 24
    biCompression =  bytes_to_i(file.read(4))   #whether compression
    biSizeImage =  bytes_to_i(file.read(4))     #picture size
    biXPelsPerMeter =  bytes_to_i(file.read(4)) #x fenbianlv
    biYPelsPerMeter =  bytes_to_i(file.read(4)) #y fenbianlv
    biClrUsed =  bytes_to_i(file.read(4))
    biClrImportant =  bytes_to_i(file.read(4))
    bit_count = biBitCount // 8
    __bitSize = biWidth * biHeight

    headermessages = {'bfType':bfType, 'bfSize':bfSize, 'bfReserved1':bfReserved1, 'bfReserved2':bfReserved2, 'bfOffBits':bfOffBits, 'biSize':biSize, 'biWidth':biWidth, 'biHeight':biHeight, 'biPlanes':biPlanes, 'biBitCount':biBitCount, 'biCompression':biCompression, 'biSizeImage':biSizeImage, 'biXPelsPerMeter':biXPelsPerMeter, 'biYPelsPerMeter':biYPelsPerMeter, 'biClrUsed':biClrUsed, 'biClrImportant':biClrImportant}
    # pixels lists
    count = 0
    bits = []
    while count < __bitSize:
        bit_count1 = 0
        key = 0
        while bit_count1 < bit_count:
            key = bytes_to_i(file.read(1))
            bits.append(key)
            bit_count1 += 1
        count += 1
    file.close()
    return headermessages, bits
