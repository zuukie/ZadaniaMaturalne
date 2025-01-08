
f = open("dane.txt", "r")
f2 = open("przyklad.txt", "r")

## 6.1
# male = 0
# female = 0
#
# for line in f:
#     line = line.strip()
#     gender = int(line[-2])
#     if gender % 2 == 0:
#         female += 1
#     else:
#         male += 1
#
# print("Mężczyzn:", male)
# print("Kobiet:", female)


## 6.2

# def getMonth(pesel):
#     month = int(pesel[2:4])
#     if month <= 12:
#         return month
#     else:
#         return month - 20
#
# count = 0
# for line in f:
#     line = line.strip()
#     if getMonth(line) == 11:
#         count += 1
#
# print(count)

## 6.3
multiply = {
    1: 1,
    2: 3,
    3: 7,
    4: 9,
    5: 1,
    6: 3,
    7: 7,
    8: 9,
    9: 1,
    10: 3,
    11: 1
}

def validate(pesel):
    score = 0
    for i in range(11):
        digit = int(pesel[i])
        score += digit * multiply[i + 1]
    return score


for line in f:
    line = line.strip()
    if validate(line) % 10 != 0:
        print(line)


f.close()
