# %%
empty_set = set()
print(empty_set)
print(type(empty_set))

# %%
techs = {'python', 'java', 'c++', 'sql'}

# %%
print(techs)

# %%
print(len(techs))

# %%
set('python')

# %%
set('aaaaaaaaale')

# %%
'python' in techs

# %%
techs.add('sas')

# %%
techs.remove('sas')

# %%
techs.pop()
techs.clear()
# %%
A = {1, 2, 3, 4, 5, 6, 7}
B = {5, 6, 7, 8, 9}
C = {5, 6}

C.issubset(A)
C.issubset([5, 7])
A.issuperset(C)
A.union(B)
A.intersection(B)
A.symmetric_difference(B)
D = A.copy()
# %%
