# %%
omega = {(a, b, c)for a in range(1, 7)for b in range(1, 7)for c in range(1, 7)}
odd = {(a, b, c)for a, b, c, in omega if a %
       2 != 0 and b % 2 != 0 and c % 2 != 0}
print(f'P-stwo: {len(odd)/len(omega):.3f}')

# %%
