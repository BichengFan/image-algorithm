def findseedfunction(grayMatrix, coordinatematrix, seedgray):
    for i, x in enumerate(grayMatrix):
        for j, y in enumerate(x):
            if y == seedgray and [i, j] in coordinatematrix:
                return [i, j]

    return [-1, -1]