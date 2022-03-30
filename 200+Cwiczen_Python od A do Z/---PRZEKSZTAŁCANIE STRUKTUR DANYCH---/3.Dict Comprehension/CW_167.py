# %%
resul = []
for k in range(1, 4):
    resul.append({key: key**k for key in range(1, 10)})
print(resul)
# ---------------------------------------------------------------
# %%
data = [{i: i**j for i in range(1, 10)} for j in range(1, 4)]
print(data)
