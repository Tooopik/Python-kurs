from math import sqrt
a = 1
b = 5
c = 4

delta = b**2 - 4*(a*c)

# pierwiastek kwadratowy bez biblioteki MATH
# delta_sqrt = delta ** (1/2)

x1 = (-b - sqrt(delta)) / (2*a)
x2 = (-b + sqrt(delta)) / (2*a)

print(f'x1 = {x1}')
print(f'x2 = {x2}')
