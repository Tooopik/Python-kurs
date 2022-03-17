# %%
probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
resoult = []

for i in probabilities:
    if i >= 0.5:
        resoult.append(1)
    else:
        resoult.append(0)

print(resoult)

# -----------------------------------------------------------
probabilities = [0.21, 0.91, 0.34, 0.55, 0.76, 0.02]
result = [1 if prob >= 0.5 else 0 for prob in probabilities]
print(result)
