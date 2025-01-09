## 5.1 5.2
f = open("liczby.txt", "r")

def isEven(number):
    if number % 2 == 0:
        return True
    return False

def palindrom(tekst):
    for i in range(len(tekst) // 2 + 1):
        if tekst[i] != tekst[-1 - i]:
            return False
    return True

maxEven = 0

for line in f:
    line = int(line.strip())
    if isEven(line):
        if line > maxEven:
            maxEven = line

    if palindrom(str(line)):
        print(line)


print("Największa parzysta:", maxEven)

f.close()

## 5.3
f = open("liczby.txt", "r")

def suma(number):
    current = 0
    for digit in number:
        current += int(digit)
    return current

calaSuma = 0

for line in f:
    line = line.strip()
    sumaCyfr = suma(line)
    if sumaCyfr > 30:
        print(line)
    calaSuma += sumaCyfr


f.close()

print("Całkowita suma:", calaSuma)