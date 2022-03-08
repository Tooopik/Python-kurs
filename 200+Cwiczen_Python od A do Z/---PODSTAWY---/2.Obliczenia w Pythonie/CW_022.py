x1, x2, x3 = 10, 11, 9
mean = (x1 + x2 + x3) / 3.0
var = ((x1 - mean)**2 + (x2 - mean)**2 + (x3 - mean)**2) / 3
std = var**(1/2)
print(f'Odchylenie standardowe zestawu danych wynosi: {std:.2f}')
