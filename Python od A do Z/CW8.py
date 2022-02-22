x = 'Programowanie w języku Python - od A do Z'
y = x.lower()
yy = y.replace('-', '')
yyy = yy.replace('ę', 'e')
yyyy = yyy.replace(' ', '')
Z = set(yyyy)

print(len(Z))

# %%
x = 'Programowanie w języku Python - od A do Z'
x = x.lower()
x = x.replace('ę', 'e')
x = x.replace(' ', '')
x = x.replace('-', '')

print(len(set(x)))

# %%
x = 'Programowanie w języku Python - od A do Z'
x = x.lower().replace('ę', 'e').replace(' ', '').replace('-', '')

print(len(set(x)))
