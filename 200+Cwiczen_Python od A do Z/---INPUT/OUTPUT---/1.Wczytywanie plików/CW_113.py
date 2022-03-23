# %%
with open('plw_d.csv', 'r') as file:
    content = file.read().splitlines()

result = []
for data in content[1:]:
    result.append(int(data.split(',')[-1]))
print(f'Max Vol: {max(result)}')
# %%
