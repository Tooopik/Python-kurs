# %%
omega = {(a, b, c)for a in range(1, 7)for b in range(1, 7)for c in range(1, 7)}
divideBySeven = {item for item in omega if (item[0]+item[1]+item[2]) % 7 == 0}
print(f'P-stwo: {len(divideBySeven)/len(omega):.2f}')
# ----------------------------------------------------------------------------------------
# %%
omega = {(x, y, z) for x in range(1, 7)
         for y in range(1, 7) for z in range(1, 7)}
a = {(x, y, z) for x, y, z in omega if (x + y + z) % 7 == 0}
prob = round(len(a) / len(omega), 2)
print(f'P-stwo: {prob}')
