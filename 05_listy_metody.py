# %%
techs = []
print(techs)

# %%
techs.append('python')
print(techs)

# %%
techs.append('java')
print(techs)

# %%
techs.append('java')
print(techs)

# %%
techs.append(['hadoop', 'spark'])
print(techs)

# %%
techs.extend(['sql', 'sas'])
print(techs)
# %%
techs.insert(0, 'go')
print(techs)
# %%
techs.insert(2, 'r')
print(techs)

# %%
print(techs)
techs.pop()
print(techs)
# %%
print(techs)
techs.pop(0)
print(techs)
# %%
print(techs.index('java'))
print(techs.index('r'))

# %%
print(techs.count('java'))
print(techs.count('r'))

# %%
techs.sort()
print(techs)
techs.sort(reverse=True)
print(techs)

# %%
techs.reverse()
print(techs)

# %%
techs[1] = 'c++'
print(techs)

# %%
