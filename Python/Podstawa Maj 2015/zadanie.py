## 5.1
# f = open("slowa.txt", "r")
#
# n = {
#     1: 0,
#     2: 0,
#     3: 0,
#     4: 0,
#     5: 0,
#     6: 0,
#     7: 0,
#     8: 0,
#     9: 0,
#     10: 0,
#     11: 0,
#     12: 0
# }
#
# def checkN(tekst):
#     count = 0
#     for letter in tekst:
#         count += 1
#     return count
#
# for line in f:
#     line = line.strip()
#     n[checkN(line)] += 1
#
# for id in n:
#     print(id, n[id])
#
# f.close()

## 5.2
f2 = open("nowe.txt", "r")

def mirror(tekst):
    new = ""
    for i in range(len(tekst)):
        new += tekst[-1 - i]
    return(new)


for line in f2:
    line = line.strip()
    mirrored = mirror(line)
    appears = 0
    mirrors = 0

    f = open("slowa.txt", "r")
    for word in f:
        word = word.strip()
        if word == line:
            appears += 1
        if word == mirrored:
            mirrors += 1
    f.close()

    print(line, appears, mirrors)


f.close()
f2.close()