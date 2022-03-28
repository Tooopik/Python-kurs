# %%
def maximum(a, b, c):
    if a >= b:
        if a >= c:
            return a
    elif b > c:
        return b
    else:
        return c


print(maximum(1, 2, 2))

# ----------------------------------------------
# %%


def maximum(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= z:
        return y
    else:
        return z
