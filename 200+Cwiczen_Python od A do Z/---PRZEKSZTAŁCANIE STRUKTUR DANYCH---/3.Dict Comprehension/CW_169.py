# %%
indeks = ['WIG20', 'mWIG40', 'sWIG80']
print({n: indeks[n]for n in range(3)})
# ------------------------------------------------------
# %%
indeks = ['WIG20', 'mWIG40', 'sWIG80']
data = {key: val for key, val in enumerate(indeks)}
print(data)
