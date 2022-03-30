# %%
data = dict(zip(('a', 'b', 'c', 'd', 'e', 'f'), (1, 2, 3, 4, 5, 6)))
dataList = [[key, data[key]]for key in data.keys()]
print(dataList)
# ---------------------------------------------------------------
# %%
data = dict(zip(('a', 'b', 'c', 'd', 'e', 'f'), (1, 2, 3, 4, 5, 6)))
result = [[key, val] for key, val in data.items()]
print(result)
