# %%
omega = {(a, b) for a in range(1, 7) for b in range(1, 7)}
square = {pair for pair in omega if pair[0]**2 + pair[1]**2 >= 45}
print(f'P-stwo: {len(square)/len(omega):.2f}')

# %%
