# 4.1
f = open("liczby.txt", "r")
f2 = open("przyklad.txt", "r")

count = 0

def isRising(list):
    first, second, third = int(line[0]), int(line[1]), int(line[2])
    return True if first < second < third else False



for line in f:
    line = line.strip().split()
    if isRising(line):
        count += 1

f.close()

print(count)

# 4.2
f = open("liczby.txt", "r")

sumEverything = 0

def NWD(a, b):
    return b if a % b == 0 else NWD(b, a % b)


for line in f:
    line = line.strip().split()
    first = NWD(int(line[0]), int(line[1]))
    second = NWD(first, int(line[2]))
    sumEverything += second

f.close()

print(sumEverything)

# 4.3

f = open("liczby.txt", "r")

count35 = 0

def sumDigits(a, b, c):
    suma = 0
    for digit in a:
        suma += int(digit)
    for digit in b:
        suma += int(digit)
    for digit in c:
        suma += int(digit)
    return suma

highest = 0
times = 0

for line in f:
    line = line.strip().split()
    suma = sumDigits(line[0], line[1], line[2])
    if suma == 35:
        count35 += 1

    if suma > highest:
        highest = suma
        times = 1
    elif suma == highest:
        times += 1


f.close()
print(count35)
print(highest)
print(times)