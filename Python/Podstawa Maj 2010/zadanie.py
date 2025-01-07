def palindrom(word):
    for i in range(len(word)):
        if word[i] != word[-1 - i]:
            return False
    return True

f = open("../Dane/dane.txt", "r")

for line in f:
    line = line.strip()
    if palindrom(line):
        print(line)

f.close()
