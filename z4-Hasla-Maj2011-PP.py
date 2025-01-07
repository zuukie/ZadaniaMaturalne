# Odpowiedzi:
#


f = open("hasla.txt", "r")

parzyste = 0
nieparzyste = 0

for line in f:
    line = line.strip()
    print(line)

    if len(line) % 2 == 0:
        parzyste += 1
    else:
        nieparzyste += 1


f.close()

print(parzyste)
print(nieparzyste)