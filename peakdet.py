def peakdetfunction(counts, delta, gray):
    maxtab = []
    mintab = []
    mn = float("inf")
    mx = float("-inf")
    # if mx < 0:
        # print("test")
    mnpos = -1
    mxpos = -1
    lookformax = 1
    count = 0
    while(count < len(counts)):
        temp = counts[count]
        # print(temp)
        if temp > mx:
            mx = temp
            mxpos = gray[count]
        if temp < mn:
            mn = temp
            mnpos = gray[count]

        if(lookformax == 1):
            if temp < mx - delta:
                maxtab.append([mxpos, mx])
                mn = temp
                mnpos = gray[count]
                lookformax = 0
        else:
            if temp > mn + delta:
                mintab.append([mnpos, mn])
                mx = temp
                mxpos = gray[count]
                lookformax = 1
        count += 1

    return maxtab, mintab