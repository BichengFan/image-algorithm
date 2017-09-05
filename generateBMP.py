def i_to_bytes(number, length, byteorder='little'):
    return number.to_bytes(length, byteorder)

def generateBMPfunction( filename,headersmessges, rgbmatrix):
    file3 = open(filename, 'wb+')
# reconstruct File Header
    file3.write(i_to_bytes(headersmessges['bfType'], 2))
    file3.write(i_to_bytes(headersmessges['bfSize'], 4))
    file3.write(i_to_bytes(headersmessges['bfReserved1'], 2))
    file3.write(i_to_bytes(headersmessges['bfReserved2'], 2))
    file3.write(i_to_bytes(headersmessges['bfOffBits'], 4))
# reconstruct bmp header
    file3.write(i_to_bytes(headersmessges['biSize'], 4))
    file3.write(i_to_bytes(headersmessges['biWidth'], 4))
    file3.write(i_to_bytes(headersmessges['biHeight'], 4))
    file3.write(i_to_bytes(headersmessges['biPlanes'], 2))
    file3.write(i_to_bytes(headersmessges['biBitCount'], 2))
    file3.write(i_to_bytes(headersmessges['biCompression'], 4))
    file3.write(i_to_bytes(headersmessges['biSizeImage'], 4))
    file3.write(i_to_bytes(headersmessges['biXPelsPerMeter'], 4))
    file3.write(i_to_bytes(headersmessges['biYPelsPerMeter'], 4))
    file3.write(i_to_bytes(headersmessges['biClrUsed'], 4))
    file3.write(i_to_bytes(headersmessges['biClrImportant'], 4))
# reconstruct pixels

    for bit in rgbmatrix:
        for bit1 in bit:
            for bit2 in bit1:
                file3.write(i_to_bytes(bit2, 1))

    file3.close()