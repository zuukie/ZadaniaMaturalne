# 6.1

# f= open("dane_6_1.txt", "r")
# def szyfruj(slowo):
#     k = 107
#     output = ""
#     for litera in slowo:
#         ascii = ord(litera)
#         new = ascii + k
#         while new > 90:
#             new -= 26
#         output += chr(new)
#     print(output)
#
# for line in f:
#     line = line.strip()
#     szyfruj(line)
#
# f.close()

# 6.2

# f = open("dane_6_2.txt", "r")
#
# def odszyfruj(slowo, k):
#     output = ""
#     for litera in slowo:
#         ascii = ord(litera)
#         new = ascii - k
#         while new < 65:
#             new += 26
#         output += chr(new)
#     return output
#
# for line in f:
#     line = line.strip().split()
#     try:
#         print(odszyfruj(line[0], int(line[1])))
#     except:
#         print(odszyfruj(line[0], 0))
#
# f.close()

# 6.3
f = open("dane_6_3.txt", "r")

def poprawne(wejscie, wyjscie):
    k = None
    for i in range(len(wejscie)):
        zWejscia = ord(wejscie[i])
        zWyjscia = ord(wyjscie[i])
        roznica = zWyjscia - zWejscia
        if roznica < 0:
            roznica += 26
        if k is None:
            k = roznica
        else:
            if k != roznica:
                return False
    return True


for line in f:
    line = line.strip().split()
    if not poprawne(line[0], line[1]):
        print(line[0])


f.close()