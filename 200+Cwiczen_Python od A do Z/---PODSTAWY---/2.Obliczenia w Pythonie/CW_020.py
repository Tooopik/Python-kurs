numbers = [4, 3, 4.5, 5]
mul = 0
for number in numbers:
    if mul != 0:
        mul *= number
    else:
        mul = numbers[0]

print(f'Średnia geometryczna podanych liczb: {mul ** (1/len(numbers)):.2f}')

# ================================================

x1, x2, x3, x4 = 4, 3, 4.5, 5
geo = (x1 * x2 * x3 * x4)**(1/4)
print(f'Średnia geometryczna podanych liczb: {geo:.2f}')
