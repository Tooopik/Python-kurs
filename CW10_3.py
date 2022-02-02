# %%
numbers = [23, 12, 53, 13, 65, 1, 45]
wartosc = 13
idx = 0
flaga = False

while idx < len(numbers):
    if numbers[idx] == wartosc:
        flaga = True
        break
    idx += 1

if flaga == False:
    print('Nieznaleziono')
else:
    print('Znaleziono')

# %%
