# Odpowiedzi:
# a) Liczb parzystych: 105; Liczb nieparzystych: 95
# b)
# dompmod
# grafarg
# kajak
# komok
# matam
# mpoopm
# mpouiuopm
# oddo
# omo
# pokop
# plkjjklp
# pokkop
# plolp
# c)
# amodda
# damod
# damodd
# dompmod
# edamo
# edamod
# isksad
# iughd
# kisksa
# kkompo
# komok
# kompiel
# kompo
# kompoc
# kompok
# kompoot
# kompooto
# kompost
# kompot
# komput
# komu
# komunikat
# moddam
# nruiugh
# nruiughd
# okisks
# okkomp
# omnibus
# omo
# ompioroip
# ompoci
# ompokk
# ompooto
# ompootoo
# ruiughd
# ruiughdf
# sokisk
# sunruiug
# ughdf
# ughdfbk
# uiughdf
# uiughdfb
# unruiug
# unruiugh
# zedamo
# plkjjklp
# mops
# polewa
# komputer
# komputerek
# kolomp
# plomp
# plolp
# komput

# # Rozwiązanie podpunktu a)
f = open("Dane/hasla.txt", "r")
parzyste = 0
nieparzyste = 0

for line in f:
    line = line.strip()
    if len(line) % 2 == 0:
        parzyste += 1
    else:
        nieparzyste += 1
f.close()

print("Podpunkt a)")
print("Liczb parzystych:", parzyste)
print("Liczb nieparzystych:", nieparzyste)
print("")


# Rozwiązanie podpunktu b)
def czyPalindrom(word):
    for i in range(len(word) // 2):
        if word[i] != word[-1 - i]:
            return False
    return True

f = open("Dane/hasla.txt", "r")
print("Podpunkt b)")

for line in f:
    line = line.strip()
    if czyPalindrom(line):
        print(line)

f.close()
print("")

# Rozwiązanie podpunktu c)
f = open("Dane/hasla.txt", "r")
print("Podpunkt c)")

def count(word):
    for i in range(len(word) - 1):
        znak1 = ord(word[i])
        znak2 = ord(word[i + 1])
        if znak1 + znak2 == 220:
            return True
    return False

for line in f:
    line = line.strip()
    if count(line):
        print(line)

f.close()
