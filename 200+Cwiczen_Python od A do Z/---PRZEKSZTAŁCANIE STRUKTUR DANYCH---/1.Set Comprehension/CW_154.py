# %%
omega = {(a, b, c) for a in range(1, 7)
         for b in range(1, 7) for c in range(1, 7)}
square = {(a, b, c) for a, b, c in omega if (a**2+b**2+c**2) % 3 == 0}
print(f'P-stwo: {len(square)/len(omega):.4f}')

# %%
