# remeber exchange int type to float type
import statistics
def Matrixstdfuntion(grayMatrix):
    stddev = []
    columnMatrix = []
    tempcolumnMatrix = list(zip(*grayMatrix))
    for x in tempcolumnMatrix:
        columnMatrix.append(list(x))

    for x in columnMatrix:
        stddev.append(statistics.stdev(x))
    print(stddev)
    meanstddev = statistics.mean(stddev)
    return meanstddev

# test
'''
aa = [[1, 2.5, 3, 4, 5, 6],[2.3, 8.7, 9, 10, 11, 12], [5.5, 14.3, 15, 16, 17, 18]]
wholemean = Matrixstdfuntion(aa)
print(wholemean)
print(statistics.stdev([1, 2.3, 5.5]))
print(statistics.stdev([2.5, 8.7, 14.3]))'''
