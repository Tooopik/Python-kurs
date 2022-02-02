# %%
saldo = 10000
klient_zweryfikowany = True

amount = int(input('Ile gotówki chcesz wypłacic?'))

if saldo > 0 and klient_zweryfikowany and saldo > amount:
    print('Możesz wypłacić')
else:
    print('Nie możesz wypłacic.'
          'Brak wystarczającej kwoty {}'.format(abs(saldo - amount)))

# %%
tech = 'python'
if tech == 'python':
    print('dobry wybor')
else:
    print('Poszukaj czegoś lepszego')
# %%
#  x if [warunek] else y

print('dobry wybor') if tech == 'python' else print(
    'Poszukaj czegos leposzego')

# %%
