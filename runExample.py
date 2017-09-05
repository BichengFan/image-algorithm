#　obtain pixel list, bitslist
import readpixel
image = 'G:\pythoncode\segmentationpitre\\4.bmp'
headers_messge, bits_list = readpixel.readpixelfunction(image)
# print(headersmessge)

# exchange to RGB matrix, rgbMatrix
import listtoMatrix
rgb_Matrix = listtoMatrix.listtoMatrixfunction(headers_messge['biWidth'], headers_messge['biHeight'], 3, bits_list)
# print(len(rgbMatrix), len(rgbMatrix[0]))

# obtain graylist, graylist
import graylist
gray_list_from_rgbMatrix = graylist.obtaingraylist(rgb_Matrix)

# obtain gray matrix, grayMatrix
gray_Matrix = listtoMatrix.listtoMatrixfunction(headers_messge['biWidth'], headers_messge['biHeight'], 1, gray_list_from_rgbMatrix)
# print(len(grayMatrix), len(grayMatrix[0]))
# obtain gray counts list and gray list
import grayandcount
signal_graylist, counts_list, counts_gray_list = grayandcount.obtaincountgray(gray_Matrix)
# test countslist
# sumcount = 0
# for x in countslist:
#     sumcount += x[1]
# print(sumcount)
# obtain count peaks list， peaks_maxtab
import peakdet
peaks_maxtab, peaks_mintab = peakdet.peakdetfunction(counts_list, 100, signal_graylist)
# two marked matrix: visitedMatrix, regionMatrix. visitedMatrix describes whether this pixel have been visited or not, and regionMatrix describes what this pixel belongs to.
'''zero_list = []
i = 0
while i < len(gray_list_from_rgbMatrix):
    zero_list.append(0)
    i += 1

print("in-----------------------------------------------------------in")'''
# possessed_Matrix = [[0 for i in range(headers_messge['biWidth'])] for j in range(headers_messge['biHeight'])]
# region_Matrix = [[0 for i in range(headers_messge['biWidth'])] for j in range(headers_messge['biHeight'])]

# test
# print(len(visited_Matrix), len(visited_Matrix[0]))
# print(len(region_Matrix), len(region_Matrix[0]))
# obtain sorted seed's pixel
# ensure sorted function compare the first item
def ensurecompareitem(item):
    return item[1]
sorted_peaks_maxtab = sorted(peaks_maxtab, key = ensurecompareitem, reverse= True)

# print(sorted_peaks_maxtab)
# seprate seed pixels from sorted_peaks_maxtab
seed_pixel_list = [row[0] for row in sorted_peaks_maxtab]
# print(seed_pixel)

# obtain average value of every column Standard deviation
import standarddev
wholemean = standarddev.Matrixstdfuntion(gray_Matrix)
print(wholemean)

# solve present segmentation average value
'''def grayMeanfromcoordMatrix(coordMatrix, grayMatrix):
    graysum = 0
    graynum = 0
    mean = 0
    for x in coordMatrix:
        graysum += grayMatrix[x[0]][x[1]]
        graynum += 1
    mean = graysum * 1.0 /graynum
    return mean'''

# generate coordinate Matrix
coordinate_Matrix = []
row_count = 0
while row_count < headers_messge['biHeight']:
    col_count = 0
    temp = []
    while col_count < headers_messge['biWidth']:
        temp.append([row_count, col_count])
        col_count += 1
    coordinate_Matrix.extend(temp)
    row_count += 1
# region growing algorithm
# determin seed
import findseed
from collections import deque
ith = 0
allsegments_list = []
# segmentation_label = 'a'
while ith < len(seed_pixel_list):
    print("____________________________________________________________________________", ith)
    present_seed = findseed.findseedfunction(gray_Matrix, coordinate_Matrix, seed_pixel_list[ith])
    if present_seed[0] == -1 or present_seed[1] == -1:
        ith += 1
        continue
    else:
        # possessed_Matrix[present_seed[0]][present_seed[1]] = 1
        # region_Matrix[present_seed[0]][present_seed[1]] = 'a'
        temp_segmentation_ele = [present_seed]
        # remember deque([seed_pixel_list[ith]])
        queue_seed = deque([present_seed])
        coordinate_Matrix.remove(present_seed)

        #
        last_count = 1
        last_sum = gray_Matrix[present_seed[0]][present_seed[1]] * 1.0
        while queue_seed:
            # print(queue_seed)
            present_seed_centre = queue_seed.popleft()
            print("present_seed_centre", present_seed_centre)
            if present_seed_centre[0] + 1 < len(gray_Matrix):
                temp_mean = last_sum / last_count
                if [present_seed_centre[0] + 1, present_seed_centre[1]] in coordinate_Matrix and abs(temp_mean - gray_Matrix[present_seed_centre[0] + 1][present_seed_centre[1]]) <= wholemean: # and possessed_Matrix[present_seed_centre[0] + 1][present_seed_centre[1]] == 0
                    queue_seed.append([present_seed_centre[0] + 1, present_seed_centre[1]])
                    # region_Matrix[present_seed_centre[0] + 1][present_seed_centre[1]] = segmentation_label
                    # possessed_Matrix[present_seed_centre[0] + 1][present_seed_centre[1]] = 1
                    temp_segmentation_ele.append([present_seed_centre[0] + 1, present_seed_centre[1]])
                    coordinate_Matrix.remove([present_seed_centre[0] + 1, present_seed_centre[1]])
                    last_sum = temp_mean * last_count + gray_Matrix[present_seed_centre[0] + 1][present_seed_centre[1]]
                    last_count += 1


            if present_seed_centre[0] + 1 < len(gray_Matrix)and present_seed_centre[1] + 1 < len(gray_Matrix[present_seed_centre[0] + 1]):
                temp_mean = last_sum / last_count
                if [present_seed_centre[0] + 1, present_seed_centre[1] + 1] in coordinate_Matrix and abs(temp_mean - gray_Matrix[present_seed_centre[0] + 1][present_seed_centre[1] + 1]) <= wholemean: # and possessed_Matrix[present_seed_centre[0] + 1][present_seed_centre[1] + 1] == 0
                    queue_seed.append([present_seed_centre[0] + 1, present_seed_centre[1] + 1])
                    # region_Matrix[present_seed_centre[0] + 1][present_seed_centre[1] + 1] = segmentation_label
                    # possessed_Matrix[present_seed_centre[0] + 1][present_seed_centre[1] + 1] = 1
                    temp_segmentation_ele.append([present_seed_centre[0] + 1, present_seed_centre[1] + 1])
                    coordinate_Matrix.remove([present_seed_centre[0] + 1, present_seed_centre[1] + 1])
                    last_sum = temp_mean * last_count + gray_Matrix[present_seed_centre[0] + 1][present_seed_centre[1] + 1]
                    last_count += 1

            if present_seed_centre[1] + 1 < len(gray_Matrix[present_seed_centre[0]]):
                temp_mean = last_sum / last_count
                if [present_seed_centre[0], present_seed_centre[1] + 1] in coordinate_Matrix and abs(temp_mean - gray_Matrix[present_seed_centre[0]][present_seed_centre[1] + 1]) <= wholemean: # and possessed_Matrix[present_seed_centre[0]][present_seed_centre[1] + 1] == 0
                    queue_seed.append([present_seed_centre[0], present_seed_centre[1] + 1])
                    # region_Matrix[present_seed_centre[0]][present_seed_centre[1] + 1] = segmentation_label
                    #　possessed_Matrix[present_seed_centre[0]][present_seed_centre[1] + 1] = 1
                    temp_segmentation_ele.append([present_seed_centre[0], present_seed_centre[1] + 1])
                    coordinate_Matrix.remove([present_seed_centre[0], present_seed_centre[1] + 1])
                    last_sum = temp_mean * last_count + gray_Matrix[present_seed_centre[0]][present_seed_centre[1] + 1]
                    last_count += 1

            if present_seed_centre[0] - 1 > 0 and present_seed_centre[1] + 1 < len(gray_Matrix[present_seed_centre[0] - 1]):
                temp_mean = last_sum / last_count
                if [present_seed_centre[0] - 1, present_seed_centre[1] + 1] in coordinate_Matrix and abs(temp_mean - gray_Matrix[present_seed_centre[0] - 1][present_seed_centre[1] + 1]) <= wholemean: # and possessed_Matrix[present_seed_centre[0] - 1][present_seed_centre[1] + 1] == 0
                    queue_seed.append([present_seed_centre[0] - 1, present_seed_centre[1] + 1])
                    # region_Matrix[present_seed_centre[0] - 1][present_seed_centre[1] + 1] = segmentation_label
                    # possessed_Matrix[present_seed_centre[0] - 1][present_seed_centre[1] + 1] = 1
                    temp_segmentation_ele.append([present_seed_centre[0] - 1, present_seed_centre[1] + 1])
                    coordinate_Matrix.remove([present_seed_centre[0] - 1, present_seed_centre[1] + 1])
                    last_sum = temp_mean * last_count + gray_Matrix[present_seed_centre[0] - 1][present_seed_centre[1] + 1]
                    last_count += 1

            if present_seed_centre[0] - 1 > 0:
                temp_mean = last_sum / last_count
                if [present_seed_centre[0] - 1, present_seed_centre[1]] in coordinate_Matrix and abs(temp_mean - gray_Matrix[present_seed_centre[0] - 1][present_seed_centre[1]]) <= wholemean: # and possessed_Matrix[present_seed_centre[0] - 1][present_seed_centre[1]] == 0
                    queue_seed.append([present_seed_centre[0] - 1, present_seed_centre[1]])
                    # region_Matrix[present_seed_centre[0] - 1][present_seed_centre[1]] = segmentation_label
                    #　possessed_Matrix[present_seed_centre[0] - 1][present_seed_centre[1]] = 1
                    temp_segmentation_ele.append([present_seed_centre[0] - 1, present_seed_centre[1]])
                    coordinate_Matrix.remove([present_seed_centre[0] - 1, present_seed_centre[1]])
                    last_sum = temp_mean * last_count + gray_Matrix[present_seed_centre[0] - 1][present_seed_centre[1]]
                    last_count += 1

            if present_seed_centre[0] - 1 > 0 and present_seed_centre[1] - 1 > 0:
                temp_mean = last_sum / last_count
                if [present_seed_centre[0] - 1, present_seed_centre[1] - 1] in coordinate_Matrix and abs(temp_mean - gray_Matrix[present_seed_centre[0] - 1][present_seed_centre[1] - 1]) <= wholemean: # possessed_Matrix[present_seed_centre[0] - 1][present_seed_centre[1] -1] == 0
                    queue_seed.append([present_seed_centre[0] - 1, present_seed_centre[1] - 1])
                    #　region_Matrix[present_seed_centre[0] - 1][present_seed_centre[1] - 1] = segmentation_label
                    # possessed_Matrix[present_seed_centre[0] - 1][present_seed_centre[1] - 1] = 1
                    temp_segmentation_ele.append([present_seed_centre[0] - 1, present_seed_centre[1] - 1])
                    coordinate_Matrix.remove([present_seed_centre[0] - 1, present_seed_centre[1] - 1])
                    last_sum = temp_mean * last_count + gray_Matrix[present_seed_centre[0] - 1][present_seed_centre[1] - 1]
                    last_count += 1

            if present_seed_centre[1] - 1 > 0:
                temp_mean = last_sum / last_count
                if [present_seed_centre[0], present_seed_centre[1] - 1] in coordinate_Matrix and abs(temp_mean - gray_Matrix[present_seed_centre[0]][present_seed_centre[1] - 1]) <= wholemean: #  and possessed_Matrix[present_seed_centre[0]][present_seed_centre[1] -1] == 0
                    queue_seed.append([present_seed_centre[0], present_seed_centre[1] - 1])
                    # region_Matrix[present_seed_centre[0]][present_seed_centre[1] - 1] = segmentation_label
                    # possessed_Matrix[present_seed_centre[0]][present_seed_centre[1] - 1] = 1
                    temp_segmentation_ele.append([present_seed_centre[0], present_seed_centre[1] - 1])
                    coordinate_Matrix.remove([present_seed_centre[0], present_seed_centre[1] - 1])
                    last_sum = temp_mean * last_count + gray_Matrix[present_seed_centre[0]][present_seed_centre[1] - 1]
                    last_count += 1

            if present_seed_centre[0] + 1 < len(gray_Matrix) and present_seed_centre[1] - 1 > 0:
                temp_mean = last_sum / last_count
                if [present_seed_centre[0] + 1, present_seed_centre[1] - 1] in coordinate_Matrix and abs(temp_mean - gray_Matrix[present_seed_centre[0] + 1][present_seed_centre[1] - 1]) <= wholemean: # and possessed_Matrix[present_seed_centre[0] + 1][present_seed_centre[1] -1] == 0
                    queue_seed.append([present_seed_centre[0] + 1, present_seed_centre[1] - 1])
                    # region_Matrix[present_seed_centre[0] + 1][present_seed_centre[1] - 1] = segmentation_label
                    # possessed_Matrix[present_seed_centre[0] + 1][present_seed_centre[1] - 1] = 1
                    temp_segmentation_ele.append([present_seed_centre[0] + 1, present_seed_centre[1] - 1])
                    coordinate_Matrix.remove([present_seed_centre[0] + 1, present_seed_centre[1] - 1])
                    last_sum = temp_mean * last_count + gray_Matrix[present_seed_centre[0] + 1][present_seed_centre[1] - 1]
                    last_count += 1

        allsegments_list.append(temp_segmentation_ele)
        #segmentation_label = chr(ord('a') + 1)
    ith += 1
print(len(allsegments_list),allsegments_list)

# color different segmentations
for x in allsegments_list[0]:
    rgb_Matrix[x[0]][x[1]][0] = 255
    rgb_Matrix[x[0]][x[1]][1] = 0
    rgb_Matrix[x[0]][x[1]][2] = 0

for x in allsegments_list[1]:
    rgb_Matrix[x[0]][x[1]][0] = 0
    rgb_Matrix[x[0]][x[1]][1] = 255
    rgb_Matrix[x[0]][x[1]][2] = 0

for x in allsegments_list[2]:
    rgb_Matrix[x[0]][x[1]][0] = 0
    rgb_Matrix[x[0]][x[1]][1] = 0
    rgb_Matrix[x[0]][x[1]][2] = 255

for x in allsegments_list[3]:
    rgb_Matrix[x[0]][x[1]][0] = 255
    rgb_Matrix[x[0]][x[1]][1] = 255
    rgb_Matrix[x[0]][x[1]][2] = 255

for x in allsegments_list[4]:
    rgb_Matrix[x[0]][x[1]][0] = 0
    rgb_Matrix[x[0]][x[1]][1] = 0
    rgb_Matrix[x[0]][x[1]][2] = 0
# sava picture
import generateBMP
generateBMP.generateBMPfunction('G:\pythoncode\\result\\4_seg.bmp', headers_messge, rgb_Matrix)

# exchange bmp to png
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mping

img = Image.open('G:\pythoncode\\result\\4_seg.bmp')
img.save("G:\pythoncode\\result\\4_seg.png")
img.close()
img1 = Image.open('G:\pythoncode\segmentationpitre\\4.bmp')
img1.save('G:\pythoncode\\result\\4.png')
img1.close()

# display png picture
imgmat = mping.imread('G:\pythoncode\\result\\4_seg.png')
imgmat1 = mping.imread('G:\pythoncode\\result\\4.png')
plt.subplot(1, 2, 1)
implot1 = plt.imshow(imgmat1)
plt.subplot(1, 2, 2)
implot1 = plt.imshow(imgmat)
plt.show()
plt.close()
