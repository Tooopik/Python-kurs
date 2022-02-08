# %%
stocks = {'AMZN.US': 'Amazon.com Inc', 'GOOGL.US': 'Alphabet Inc',
          'AAPL.US': 'Apple Inc', 'UBER.US': 'Uber Technologies Inc', 'MSFT.US': 'Microsoft Corp'}


# %%
stocks.keys()

# %%
stocks.values()

# %%
stocks.items()

# %%
for key, value in stocks.items():
    print('{:8}: {}'.format(key, value))

# %%
stocks_dict = {key: value for (key, value) in stocks.items()}

# %%
stocks_set = {(key, value) for (key, value) in stocks.items()}

# %%
stocks_invert = {value: key for (key, value) in stocks.items()}

# %%
stocks_lower = {key.lower(): value for (key, value) in stocks.items()}

# %%
stocks_length = {key: len(value) for (key, value) in stocks.items()}

# %%
stocks_length = {key: value + ' : ' + str(len(value))
                 for (key, value) in stocks.items()}

# %%


def replace_corp_inc(name):
    name = name.replace('Corp', '0')
    name = name.replace('Inc', '1')
    return name


stocks_flag = {k: replace_corp_inc(v) for (k, v) in stocks.items()}
# %%
stocks_corp = {key: val for (key, val) in stocks.items() if 'Corp' in val}
# %%
stocks_inc = {key: val for (key, val) in stocks.items() if 'Inc' in val}

# %%
stocks_a = {key: val for (key, val) in stocks.items() if val.startswith('A')}

# %%
stocks_a_13 = {key: val for (key, val) in stocks.items()
               if val.startswith('A') if len(val) < 13}

# %%
