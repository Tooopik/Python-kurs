# %%
KOD_PIN = '0000'
pin = ''
counter = 0

while pin != KOD_PIN and counter < 3:
    pin = input('Wprowadź kod pin: ')
    if pin == KOD_PIN:
        print('Zalogowany')
        break
    counter += 1
else:
    print('Zbyt duzo prób!')


# %%
