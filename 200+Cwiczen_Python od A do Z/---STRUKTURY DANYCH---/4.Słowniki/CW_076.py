# %%
stats = {'strona': 'e-smartdata.org', 'ruch': 100, 'typ': 'organiczny'}
stats.pop('ruch')
print(stats)

# ----------------------------------------------------------------------
stats = {'strona': 'e-smartdata.org', 'ruch': 100, 'typ': 'organiczny'}
del stats['ruch']
print(stats)
