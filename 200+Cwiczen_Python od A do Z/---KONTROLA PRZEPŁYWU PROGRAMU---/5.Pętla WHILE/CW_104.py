#%%
n = 1
pv = 1000
r = 0.04
fv = 0

while fv < pv*2:
    n+=1
    fv = pv*(1+r)**n
    


print(f'Wartość przyszła: {fv:.2f} PLN. Liczba okresów: {n} lat')
# %%
