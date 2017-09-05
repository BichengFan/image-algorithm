def obtaincountgray(grayMatrix):
    graylist = list(range(0, 256))
    countlist = []
    grayandlist = []

    for x in graylist:
        tempcount = 0
        for y in grayMatrix:
            tempcount +=  y.count(x)
        grayandlist.append([x, tempcount])
        countlist.append(tempcount)
    return graylist, countlist, grayandlist
