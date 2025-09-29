## Podpunkt a)
f = open("napisy.txt", "r")

countParzyste = 0

def parzysta(number):
    if len(number) % 2 == 0:
        return True
    else:
        return False

for line in f:
    line = line.strip()
    if parzysta(line):
        countParzyste += 1

print(countParzyste)

f.close()

## Podpunkt b)
f = open("napisy.txt", "r")

counter = 0

def checkZeroOnes(text):
    global counter
    countZeros = 0
    countOnes = 0
    for digit in text:
        if digit == "1":
            countOnes += 1
        elif digit == "0":
            countZeros += 1
    if countOnes == countZeros:
        counter += 1


for line in f:
    line = line.strip()
    if checkZeroOnes(line):
        counter += 1

print(counter)
f.close()


## Podpunkt c)
f = open("napisy.txt", "r")

count0 = 0
count1 = 0


def goThrough(text):
    global count0
    global count1
    firstDigit = text[0]
    for i in range(len(text) - 1):
        nextDigit = text[i + 1]
        if nextDigit != firstDigit:
            return False
        firstDigit = nextDigit
    if firstDigit == "1":
        count1 += 1
    elif firstDigit == "0":
        count0 += 1




for line in f:
    line = line.strip()
    goThrough(line)

f.close()

print("Same zera:", count0)
print("Same jedynki:", count1)

## Podpunkt d)
f = open("napisy.txt", "r")

options = {
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    10: 0,
    11: 0,
    12: 0,
    13: 0,
    14: 0,
    15: 0,
    16: 0
}

for line in f:
    line.strip()
    k = len(line) - 1
    options[k] += 1

f.close()
print(options)