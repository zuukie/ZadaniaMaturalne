# Odpowiedzi:
# 5041
# 1369
# 32041
# 844561
# 4
# 96721
# 9
# 942841
# 49
# 1849
# 528529
# 121
# 961
# 169

F = open("Dane/liczby.txt", "r")

def liczbaPierwsza(number):
    for i in range(2, int(number**(1/2)) + 1):
        if number % i == 0:
            return False
    return True

for line in F:
    line = int(line.strip())
    pierwiastek = line**(1/2)

    if pierwiastek == int(pierwiastek):
        if line > 1 and liczbaPierwsza(int(pierwiastek)):
            print(line)


F.close()


