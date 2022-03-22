# %%
value = 0
days = 0
try:
    with open('playway.txt', 'r') as file:
        content = file.read().split('\n')
    for record in content[1:]:
        data = record.split(',')
        value += int(data[4])
        days += 1

    print(f'3-dniowa średnia cena zamknięcia: {value/days:.2f}')


except FileNotFoundError:
    print('Nie znaleziono pliku')

# %%
# -------------------------------------------------------------------------------------------------------------------
with open('playway.txt', 'r') as file:
    lines = file.read().splitlines()
    # print(lines)

close = []

for idx, line in enumerate(lines):
    # print(idx)
    # print(line)
    if idx > 0:
        close.append(int(line.split(',')[-2]))
        # print(close)

close_avg = sum(close) / len(close)
print(f'3-dniowa średnia cena zamknięcia: {close_avg:.2f}')

# %%
