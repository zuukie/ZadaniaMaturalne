# # 4.1

f = open("sygnaly.txt", "r")
f2 = open("przyklad.txt", "r")

lineCount = 0
output = ""
for line in f:
    line = line.strip()
    lineCount += 1
    if lineCount % 40 == 0:
        output += line[9]

f.close()
f2.close()

print(output)

# # 4.2
f = open("sygnaly.txt", "r")
f2 = open("przyklad.txt", "r")

bestScore = 0
bestWord = None

for line in f:
    currWord = line.strip()
    letters = []
    currScore = 0
    for letter in currWord:
        if letter not in letters:
            letters.append(letter)
            currScore += 1
    if currScore > bestScore:
        bestScore = currScore
        bestWord = currWord

f.close()
f2.close()

print(bestWord, bestScore)

# 4.3
f = open("sygnaly.txt", "r")
f2 = open("przyklad.txt", "r")

def specialWord(text):
    text = sorted(text)
    if ord(text[len(text) - 1]) - ord(text[0]) <= 10:
        return True
    return False

for line in f:
    line = line.strip()
    if specialWord(line):
        print(line)

f.close()
f2.close()
