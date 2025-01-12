# 6.1
f = open("dane4.txt", "r")

def pierwsza(number):
    for i in range(2, int(number**(1/2)) + 1):
        if number % i == 0:
            return False
    return True

counter = 0
highest = 0
lowest = 30001
before = None

countBlizniak = 0

for line in f:
    line = int(line.strip())
    # if pierwsza(line):
    #     counter += 1

    # if pierwsza(line):
    #     if line > highest:
    #         highest = line
    #     elif line < lowest:
    #         lowest = line

    if before is None:
        before = line
        continue

    if abs(line - before) == 2:
        if pierwsza(before) and pierwsza(line):
            print(before, "i", line)
            countBlizniak += 1

    before = line

f.close()

print(countBlizniak)
# print(lowest)
# print(highest)
