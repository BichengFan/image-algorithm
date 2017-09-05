# exchange to float32
def exchangeGray(list):
    gray = (list[0] * 299 + list[1] * 587 + list[2] * 114) // 1000
    return gray

def obtaingraylist(rgbmatrix):
    graylist = []
    for x in rgbmatrix:
        for y in x:
            graylist.append(exchangeGray(y))

    return graylist


