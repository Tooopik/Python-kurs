# %%
stocks = [
    {'indeks': 'mWIG40', 'name': 'TEN', 'price': 304},
    {'indeks': 'mWIG40', 'name': 'PLW', 'price': 309},
    {'indeks': 'sWIG80', 'name': 'BBT', 'price': 22}
]
result = []
[result.append(i) for i in stocks if i['indeks'] == 'mWIG40']
print(result)

# %%
print(list(filter(lambda item: item['indeks'] == 'mWIG40', stocks)))
