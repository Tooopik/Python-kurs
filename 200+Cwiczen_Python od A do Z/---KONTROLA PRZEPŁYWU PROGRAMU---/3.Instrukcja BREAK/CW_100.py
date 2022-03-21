# %%
number = 13

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            print(f'{number} - nie jest pierwsza')
            break
    else:
        print(f'{number} - liczba pierwsza')
else:
    print(f'{number} - nie jest pierwsza')
