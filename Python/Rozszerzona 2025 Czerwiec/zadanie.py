def checkIfNum(letter):
    if 48 <= ord(letter) <= 57:
        return True
    return False

# Zadanie 1
file = open("dane.txt", "r")

text = ""
for line in file:
    line = line.strip()
    text = line
file.close()

count = 0
toCount = False
for i in range(2, len(text)):
    if toCount:
        if checkIfNum(text[i]):
            continue
        else:
            toCount = False
            continue
    elif checkIfNum(text[i-2]) == False and (text[i-1] == "5" and text[i] == "0"):
        toCount = True
        count += 1

print("ZADANIE 1")
print(count)

# Zadanie 2
file = open("dane.txt", "r")

text = ""
for line in file:
    line = line.strip()
    text = line
file.close()

ranking = {}

for letter in text:
    if not checkIfNum(letter):
        continue
    else:
        if letter in ranking:
            ranking[letter] += 1
        else:
            ranking[letter] = 1
print("ZADANIE 2")
print(ranking)

# Zadanie 3 i 4
file = open("dane.txt", "r")

text = ""
for line in file:
    line = line.strip()
    text = line
file.close()

numery = []
startCount = False
currentText = ""
currentLength = 0

for i in range(len(text)):
    if not checkIfNum(text[i]):
        if currentLength == 9:
            numery.append(currentText)
        currentText = ""
        currentLength = 0
        startCount = False
        continue
    else:
        if startCount:
            currentText += text[i]
            currentLength += 1
            continue
        else:
            if not checkIfNum(text[i-1]):
                startCount = True
                currentLength = 1
                currentText = text[i]

print("ZADANIE 3")
startsWith5 = []
for number in numery:
    if number[0] == "5":
        startsWith5.append(number)
        print(number)

for i in range(len(numery)):
    numery[i] = [numery[i], []]
    for letter in numery[i][0]:
        if letter not in numery[i][1]:
            numery[i][1].append(letter)
    numery[i] = [numery[i][0], len(numery[i][1])]

currLowest = 10
currList = []
for numer in numery:
    if numer[1] < currLowest:
        currLowest = numer[1]
        currList = [numer[0]]
    elif numer[1] == currLowest:
        currList.append(numer[0])

print("ZADANIE 4")
print(currLowest, currList)
