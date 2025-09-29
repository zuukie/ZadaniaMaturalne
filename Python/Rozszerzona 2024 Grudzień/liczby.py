# f = open("liczby.txt", "r")
# f2 = open("liczby_przyklad.txt", "r")
#
# def isKwadratem(n):
#     pierwiastek = n**(1/2)
#     if int(pierwiastek)**2 == n:
#         return True
#     return False
#
# counter = 0
#
# for line in f:
#     line = int(line.strip())
#     if isKwadratem(line):
#         counter += 1
#         if counter == 1:
#             print(line)
#
#
# f.close()
# f2.close()
# print(counter)
#
# f = open("liczby.txt", "r")
# f2 = open("liczby_przyklad.txt", "r")
#
# def highest(list):
#     result = ""
#     for i in range(len(list)):
#         highestDigit = max(list)
#         list.remove(highestDigit)
#         result += str(highestDigit)
#     return result
#
# def lowest(list):
#     result = ""
#     for i in range(len(list)):
#         lowestDigit = min(list)
#         list.remove(lowestDigit)
#         result += str(lowestDigit)
#     return result
#
# lowerThan = 0
# higherThan = 0
# equal = 0
#
# for line in f:
#     line = line.strip()
#     for i in range(2):
#         if i == 0:
#             digits = []
#             for letter in line:
#                 digits.append(int(letter))
#             high = int(highest(digits))
#         else:
#             digits = []
#             for letter in line:
#                 digits.append(int(letter))
#             low = int(lowest(digits))
#     roznica = high - low
#     if roznica == int(line):
#         print(roznica)
#         equal += 1
#     elif roznica > int(line):
#         higherThan += 1
#     else:
#         lowerThan += 1
#
# f.close()
# f2.close()
#
# print("Mniejsze:", lowerThan)
# print("Równe:", equal)
# print("Większe:", higherThan)

f = open("liczby.txt", "r")
f2 = open("liczby_przyklad.txt", "r")

def distinct(list):
    newList = []
    for el in list:
        if el not in newList:
            newList.append(el)
    return len(newList)

def dzielniki(n):
    dzielnik = []
    p = 2
    while n > 1:
        if n % p == 0:
            n = n // p
            dzielnik.append(p)
        else:
            p += 1
    return distinct(dzielnik)


for line in f:
    line = int(line.strip())
    if dzielniki(line) >= 5:
        print(line)
f.close()
f2.close()