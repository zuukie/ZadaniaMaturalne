file1 = open("./instrukcje.txt", "r")
test = open("./przyklad.txt", "r")

steps = []
letters = []

for line in file1:
    line = line.strip().split()
    steps.append(line[0])
    letters.append(line[1])

file1.close()

# 4.1
length = 0
for el in steps:
    if el == "DOPISZ":
        length += 1
    elif el == "USUN":
        length -= 1
print(length)

# 4.2
current = 1
currentType = ""
highest = 0
highestType = ""

for i in range(len(steps) - 1):
    if steps[i] == steps[i+1]:
        current += 1
    else:
        if current >= highest:
            highest = current
            highestType = currentType
        current = 1
        currentType = steps[i+1]
print(highestType, highest)


# 4.3
lettersType = {}

for i in range(len(steps)):
    if steps[i] != "DOPISZ":
        continue
    if letters[i] not in lettersType:
        lettersType[letters[i]] = 1
    else:
        lettersType[letters[i]] += 1

for key in lettersType:
    highest = max(lettersType.values())
    if lettersType[key] == highest:
        print(key, highest)
        break

# 4.4
text = ""
for i in range(len(steps)):
    if steps[i] == "DOPISZ":
        text += letters[i]
    elif steps[i] == "USUN":
        text = text[0:-1]
    elif steps[i] == "ZMIEN":
        text = text[0:-1]
        text += letters[i]
    elif steps[i] == "PRZESUN":
        for j in range(len(text)):
            if text[j] == letters[i]:
                nowaLiterka = ord(letters[i]) + 1
                if nowaLiterka == 91:
                    nowaLiterka = 65
                text = text[0:j] + chr(nowaLiterka) + text[j+1:]
                break

print(text)