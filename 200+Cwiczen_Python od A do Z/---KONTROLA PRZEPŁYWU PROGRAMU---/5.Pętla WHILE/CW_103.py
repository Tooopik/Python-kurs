# %%
def czy_pierwsza(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    pierw = int(n**0.5) + 1
    for dzielnik in range(3, pierw, 2):
        if n % dzielnik == 0:
            return False
    return True


n = 0
idx = 0
lp = ''
while True:
    n += 1
    if idx < 10:
        if czy_pierwsza(n):
            idx += 1
            if idx > 1:
                lp += ','+str(n)
            else:
                lp += str(n)
    else:
        break
print(lp)

# -----------------------------------------------------------------
counter = 0
number = 2
prime = []

while counter < 10:
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        prime.append(str(number))
        counter += 1
    number += 1

print(','.join(prime))
