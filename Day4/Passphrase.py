
lines = []

with open('Day4\input.txt', 'r') as file:
    lines = file.readlines()

# return number of valid passphrases
# valid if phrase is not repeated within line
def Part1(line):
    total = 0
    for l in line:
        passphrase = l.split()
        valid = True
        i = 0
        while i < len(passphrase) and valid: # compare phrases until end of line or found
            if passphrase.count(passphrase[i])-1 > 0:
                valid = False
            i += 1
        if valid: total += 1
    return total

# print (Part1(lines))

# valid if not anagram
def Part2(line):
    total = 0
    for l in line:
        passphrase = l.split()
        valid = True
        i = 0
        while i < len(passphrase) and valid: # compare phrases until end of line or found
            for j in range(len(passphrase)):
                if j+1 < len(passphrase) and j+1 != i: # skip duplicates
                    if ''.join(sorted(passphrase[i])) == ''.join(sorted(passphrase[j+1])): valid = False #sort letters to check for match
            i += 1
        if valid: total += 1
    return total

print (Part2(lines))