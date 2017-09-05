def listtoMatrixfunction(x, y, a, list):  # x is width
    j = 0
    N = []
    while j < y:
        i = 0
        F = []
        while i < x:
            if a == 1:
                # print(i)
                F.append(list[j * x + i])
                i += 1
            else:
                k = 0
                T = []
                while k < a:
                    T.append(list[j * x * a + a * i + k])
                    k += 1
                F.append(T)
                i += 1
        N.append(F)
        j += 1

    return N
