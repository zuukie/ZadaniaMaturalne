# # Zadanie 1
# n = 42
# i = 1
#
# while n > 0:
#     rest = n % 2
#     if rest == 1:
#         print(i)
#     n //= 2
#     i += 1

# # Zadanie 2 - Rekurencja
count = 0
def f(x, p):
    global count
    count += 1
    if x == 0:
        return 0
    else:
        c = x % p
        if c % 2 == 1:
            return f(x // p, p) + c
        else:
            return f(x // p, p) - c
# i = 0
x = 130
p = 3
print(f(x, p))
print(count)