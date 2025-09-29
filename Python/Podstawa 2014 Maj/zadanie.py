f = open("PARY_LICZB.TXT", "r")

def wielokrotnosc(x, y):
    if (x % y) == 0:
        return True
    return False

counter = 0

for line in f:
    line = line.strip().split()
    line[0], line[1] = int(line[0]), int(line[1])
    line.sort()
    if wielokrotnosc(line[1], line[0]):
        counter += 1

f.close()

print(counter)

def suma(tekst):
    cyfry = 0
    for letter in tekst:
        cyfry += int(letter)
    return cyfry

f = open("PARY_LICZB.TXT", "r")

counter = 0
for line in f:
    line = line.strip().split()
    if suma(line[0]) == suma(line[1]):
        counter += 1

f.close()

print(counter)


def NWD(a, b):
    return b if a % b == 0 else NWD(b, a % b)

f = open("PARY_LICZB.TXT", "r")

count = 0
for line in f:
    line = line.strip().split()
    line[0], line[1] = int(line[0]), int(line[1])
    if NWD(line[0], line[1]) == 1:
        count += 1

f.close()
print(count)