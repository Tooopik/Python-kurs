# %%
stocks = ['playway', 'boombit', 'cd projekt']
x = map(len, stocks)
print(list(x))

# %%
stocks = ['playway', 'boombit', 'cd projekt']
length = list(map(lambda stock: len(stock), stocks))
print(length)
# %%
