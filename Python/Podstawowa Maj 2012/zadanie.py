f = open("cyfry.txt", "r")
# Podpunkt a)
parzyste = 0
for line in f:
    line = int(line.strip())
    if line % 2 == 0:
        parzyste += 1
print(parzyste)
f.close()


f = open("cyfry.txt", "r")
# Podpunkt b)
max = [-1, -1]
min = [10000000000, -1]

for line in f:
    line = line.strip()
    suma = 0
    for cyfra in line:
        suma += int(cyfra)
    if suma > max[0]:
        max[0], max[1] = suma, line
    elif suma < min[0]:
        min[0], min[1] = suma, line


print(max)
print(min)
f.close()


f = open("cyfry.txt", "r")
# Podpunkt c)
def isASC(number):
    while number > 0:
        lastDigit = number % 10
        number //= 10
        preLastDigit = number % 10
        if preLastDigit >= lastDigit:
            return False
    return True

for line in f:
    line = int(line.strip())
    if isASC(line):
        print(line)

f.close()
