def secondElement(self):
    return self[1]


info = (('Monika', 19), ('Tomek', 21), ('Adam', 18), ('Jarek', 30))


gr = tuple(sorted(info, key=secondElement, reverse=False))
lo = tuple(sorted(info, key=secondElement, reverse=True))

print(f'Rosnąco: {gr}')
print(f'Malejąco: {lo}')


# ----------------------------------------------------------------------------
info = (('Monika', 19), ('Tomek', 21), ('Adam', 18), ('Jarek', 30))
asc = tuple(sorted(info, key=lambda item: item[1]))
desc = tuple(sorted(info, key=lambda item: item[1], reverse=True))
print(f'Rosnąco: {asc}')
print(f'Malejąco: {desc}')
