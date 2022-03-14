# %%
project_ids = {
    '01': 'open',
    '03': 'in progress',
    '05': 'in progress',
    '04': 'completed'
}
values_list = sorted(list(set(project_ids.values())))
print(values_list)

# --------------------------------------------------------
project_ids = {
    '01': 'open',
    '03': 'in progress',
    '05': 'in progress',
    '04': 'completed'
}

result = list(set(project_ids.values()))
result.sort()
print(result)
