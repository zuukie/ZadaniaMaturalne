f = open("liczby.txt", "r")

def odd(n):
    if n % 2 == 0:
        return False
    return True

counter = 0

for line in f:
    line = int(line.strip())
    if odd(line):
        counter += 1

# counter = 0
# for line in f:
#     line = line.strip()
#     if int(line) % 2 != 0:
#         counter += 1

f.close()
print(counter)


# f = open("liczby.txt", "r")
#
# def suma(tekst):
#     suma = 0
#     for literka in tekst:
#         suma += int(literka)
#     return suma
#
# for line in f:
#     line = line.strip()
#     if suma(line) == 11:
#         print(line)
#
# f.close()
#
# f = open("liczby.txt", "r")
#
# def pierwsza(n):
#     for i in range(2, n // 2):
#         if n % i == 0:
#             return False
#     return True
#
# for line in f:
#     line = int(line.strip())
#     if pierwsza(line) and 5000 >= line >= 4000:
#         print(line)
#
#
#
# f.close()