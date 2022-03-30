# %%
stocks = {'Boombit': '001', 'CD Projekt': '002', 'Playway': '003'}
print({stocks[key]: key for key in stocks})
# ---------------------------------------------------------------------
# %%
stocks = {'Boombit': '001', 'CD Projekt': '002', 'Playway': '003'}
result = {value: key for key, value in stocks.items()}
print(result)
