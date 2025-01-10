## 4.1
f = open("dane4.txt", "r")

highest = 0
lowest = 22222222222222
before = 0

for line in f:
    line = int(line.strip())
    difference = abs(line - before)
    before = line
    if difference > highest:
        highest = difference
    elif difference < lowest:
        lowest = difference

print("Zadanie 4.1")
print("Highest:", highest, "Lowest:", lowest)
print("")

f.close()

## 4.2
f = open("dane4.txt", "r")


before = None
lastGap = -1
currentLength = 0
bestLength = 0

for line in f:
    line = int(line.strip())
    if before is None:
        before = line
        currentFirst = line
        continue

    currentGap = abs(line - before)
    if currentGap == lastGap:
        currentLength += 1
        before = line
        continue
    else:
        if currentLength > bestLength:
            bestFirst = currentFirst
            bestLast = before
            bestLength = currentLength
        currentFirst = before
        currentLength = 2
        before = line
        lastGap = currentGap

print("Zadanie 4.2")
print(bestLength, bestFirst, bestLast)
print("")

f.close()

## 4.3
f = open("dane4.txt", "r")

everything = {

}

before = None
currentLength = 0

for line in f:
    line = int(line.strip())
    if before is None:
        before = line
        continue

    gap = abs(line - before)
    found = False
    # Szukamy czy ta luka ma już jakąś krotność, jeżeli ma to zwiększamy o jeden
    for id in everything:
        if everything[id].__contains__(gap):
            everything[id].remove(gap)
            found = True
            try:
                everything[id + 1].append(gap)
            except:
                everything[id + 1] = [gap]
            break

    if not found:
        try:
            everything[1].append(gap)
        except:
            everything[1] = [gap]

    before = line

f.close()

print("Zadanie 4.3")
print("Luki",  everything[max(everything)], "pojawiły się", max(everything), "razy")
print("")