import math

"""
spiral:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10  ^
21  22  23  24  25 _|

"""

# part 1
# manhattan distance from data location to square 1

def Part1(data):
    if data == 1:
        return 0

    sideLength = math.ceil(math.sqrt(data)) # side length where data is located
    if sideLength % 2 == 0: # account for even sq numbers
        sideLength += 1
    edgeToCentreDist = sideLength//2 # max vertical or horizontal distance from square 1
    edgeCentreVal = [] # middle of each side data location
    for i in range(0,4):
        edgeCentreVal.append(sideLength**2 - ((sideLength - 1)*i) - edgeToCentreDist)
    dataToCentreDist = [] # how far data is to each centre point
    for j in range(0,4):
        dataToCentreDist.append(abs(edgeCentreVal[j]-data))
    return min(dataToCentreDist) + edgeToCentreDist # want closest centre point to data

print (Part1(int(input())))