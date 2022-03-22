# %%
try:
    with open('indexy.txt', 'r', encoding='UTF-8') as file:
        content = file.readlines()
        indexes = []
        for idx in content:
            if idx.startswith("WIG"):
                index = idx.replace('\n', '')
                indexes.append(index)
    print(indexes)

except FileNotFoundError:
    print('Nie znaleziono pliku')


# %%
# ----------------------------------------------------------------------------------------------------
with open('indexy.txt', 'r') as file:
    lines = file.read().splitlines()
    print(lines)

indexes = [index for index in lines if index.startswith('WIG')]
print(indexes)
# %%
