## 1.1
f = open("mecz.txt", "r")
f2 = open("mecz_przyklad.txt", "r")
line = f.readline().strip()

counter = 0
for i in range(len(line) - 1):
    if line[i] != line[i + 1]:
        counter += 1

print("Zadanie 1.1")
print(counter)
print("")

f.close()
f2.close()

## 1.2
f = open("mecz.txt", "r")
f2 = open("mecz_przyklad.txt", "r")
line = f.readline()

winsA = 0
winsB = 0

for team in line:
    if team == "A":
        winsA += 1
    else:
        winsB += 1
    if (winsA >= 1000 or winsB >= 1000) and abs(winsA - winsB) >= 3:
        break

print("Zadanie 1.2")
if winsA > winsB:
    print("A ", winsA, ":", winsB, sep="")
else:
    print("B ", winsA, ":", winsB, sep="")
print("")

f.close()
f2.close()


# 1.3
f = open("mecz.txt", "r")
f2 = open("mecz_przyklad.txt", "r")
line = f2.readline()

wszystkiePassy = 0
dluzszaDruzyna = "" # A albo B
najdluzszaPassa = 0

ostatniWynik = "" # A albo B

for team in line:
    if ostatniWynik == "":
        ostatniWynik = team
        aktualnaPassa = 1
        continue

    if ostatniWynik == team:
        aktualnaPassa += 1
        continue

    if aktualnaPassa >= 10:
        wszystkiePassy += 1

    if aktualnaPassa > najdluzszaPassa:
        najdluzszaPassa = aktualnaPassa
        dluzszaDruzyna = ostatniWynik

    aktualnaPassa = 1
    ostatniWynik = team

print("Zadanie 1.3")
print(wszystkiePassy, dluzszaDruzyna, najdluzszaPassa)
print("")

f.close()
f2.close()