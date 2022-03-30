# %%
with open('plw.txt', 'r', encoding='UTF-8') as file:
    lines = file.read().splitlines()
words = [word.split() for word in lines if len(word) > 0]
print(words)

# %%
