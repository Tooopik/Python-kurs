# %%
with open('plw_d.csv', 'r') as file:
    content = file.read().splitlines()

result = []
for data in content[1:]:
    result.append(int(data.split(',')[-1]))
print(f'Max Vol: {max(result)}')
# %%
# ------------------------------------------------------------------
with open('plw_d.csv', 'r') as file:
    content = file.read().splitlines()

volumes = [line.split(',')[-1] for line in content][1:]
volumes = [int(vol) for vol in volumes]
max_vol = max(volumes)
print(f'Max Vol: {max_vol}')
