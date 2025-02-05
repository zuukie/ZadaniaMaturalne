# 6.1

f = open("dane.txt", "r")
f2 = open("przyklad.txt", "r")

najciemniejszyEver = 255
najjasniejszyEver = 0

for line in f:
    line = line.strip().split()
    for el in line:
        if int(el) > najjasniejszyEver:
            najjasniejszyEver = int(el)
        if int(el) < najciemniejszyEver:
            najciemniejszyEver = int(el)

f.close()
f2.close()

print(najciemniejszyEver)
print(najjasniejszyEver)

# 6.2

f = open("dane.txt", "r")
f2 = open("przyklad.txt", "r")

def pionowy(line):
    for i in range(len(line) // 2 + 1):
        if line[i] != line[-1 - i]:
            return False
    return True

count = 0
for line in f:
    line = line.strip().split()
    if not pionowy(line):
        count += 1



f.close()
f2.close()

print(count)

# 6.3
# CO TO JEST ZA ROZWIĄZANIE????

f = open("dane.txt", "r")
f2 = open("przyklad.txt", "r")

counter = 0

firstLine = None
secondLine = None
thirdLine = None

for line in f:
    line = line.strip().split()

    if firstLine is None:
        firstLine = line
        continue
    if secondLine is None:
        secondLine = line

        for i in range(len(firstLine)):
            active = int(firstLine[i])
            if i > 0:
                left = int(firstLine[i - 1])
            if i < len(firstLine) - 1:
                right = int(firstLine[i + 1])
            down = int(secondLine[i])

            if abs(active - down) > 128:
                counter += 1
                continue
            if i > 0:
                if abs(active - left) > 128:
                    counter += 1
                    continue
            if i < len(secondLine) - 1:
                if abs(active - right) > 128:
                    counter += 1
                    continue
        continue

    if thirdLine is None:
        thirdLine = line

    for i in range(len(secondLine)):
        active = int(secondLine[i])
        if i > 0:
            left = int(secondLine[i - 1])
        if i < len(secondLine) - 1:
            right = int(secondLine[i + 1])
        up = int(firstLine[i])
        down = int(thirdLine[i])

        if abs(active - up) > 128 or abs(active - down) > 128:
            counter += 1
            continue
        if i > 0:
            if abs(active - left) > 128:
                counter += 1
                continue
        if i < len(secondLine) - 1:
            if abs(active - right) > 128:
                counter += 1
                continue

    firstLine = secondLine
    secondLine = thirdLine
    thirdLine = line

for i in range(len(thirdLine)):
    active = int(thirdLine[i])
    if i > 0:
        left = int(thirdLine[i - 1])
    if i < len(thirdLine) - 1:
        right = int(thirdLine[i + 1])
    up = int(secondLine[i])

    if abs(active - up) > 128:
        counter += 1
        continue
    if i > 0:
        if abs(active - left) > 128:
            counter += 1
            continue
    if i < len(secondLine) - 1:
        if abs(active - right) > 128:
            counter += 1
            continue

f.close()
f2.close()

print(counter)


# 6.4
f = open("dane.txt", "r")
f2 = open("przyklad.txt", "r")

lines = []
bestScore = -1

for line in f:
    line = line.strip().split()
    lines.append(line)

for column in range(len(lines[0])):
    curr = 1
    for row in range(len(lines) - 1):
        if lines[row][column] == lines[row + 1][column]:
            curr += 1
        else:
            if bestScore < curr:
                bestScore = curr
            curr = 1

print(bestScore)
f.close()
f2.close()