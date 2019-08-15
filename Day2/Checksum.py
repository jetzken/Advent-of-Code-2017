import csv

checksumList = []

with open('Day2\input.txt', 'r') as file:
    reader = csv.reader(file, delimiter = '\t') # tab used as seperater of items
    for line in reader: # line is initially list of strings
        l = []
        for i in line:
            l.append(int(i))
        checksumList.append(l)

# returns sum of difference of each line
def checkSum1 (checksum): 
    total = 0
    for line in checksum:
        total += max(line) - min(line)
    return total

# returns sum of quotient of the evenly divisible values in each line
# per line there are only two numbers that will return remainder 0
def checkSum2 (checksum):
    total = 0
    for line in checksum:
        for i in line:
            for j in line:
                if i > j and i % j == 0:
                    total += i/j
    return total

print (checkSum1(checksumList))
print (checkSum2(checksumList))