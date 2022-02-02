# %%
raw_data = '345!23!874765!9837467!434343'
clean_data = ''
for i in raw_data:
    if i != '!':
        clean_data += i
    else:
        clean_data += ','
print(clean_data)
# %%
suma = 0
for i in range(10):
    suma += i
print(suma)

# %%
saldo = 450
for kwota in range(10, 60, 10):
    print('Wypłacono kwota: {}'.format(kwota))
    saldo -= kwota
    print('Saldo po wypłacie: {} '.format(saldo))

print('Saldo końcowe: {} '.format(saldo))
# %%

print('Witaj w systemie logowania.')
print('*'*30)
nick = input(' Podaj swój nick: ')
pin_code = input('Podaj PIN {}: '.format(nick))

if set(pin_code).issubset(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
    if len(pin_code) == 4:
        if pin_code == '3871' and nick == 'Tooopik':
            print('PIN OK')
        else:
            print('Kod nick lub kod PIN niewłaściwy')
    else:
        print('{} Twój kod PIN jest za krótki'.format(nick))

else:
    print('Kod PIN musi składać się z cyfr!')

# %%
