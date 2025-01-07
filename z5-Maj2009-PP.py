F = open("liczby.txt", "r")

for line in F:
    line = int(line.strip())
    print(line)
    print(type(line))


F.close()