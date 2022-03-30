# %%
with open('plw.txt', 'r', encoding="UTF-8") as file:
    lines = file.read()
words = [word.lower().replace(',', '').replace('.', '')
         for word in lines.split()]
words = [word for word in words if len(word) >= 8]
print(sorted(words))

# -------------------------------------------------------------------
# %%
with open('plw.txt', 'r') as file:
    lines = file.read()

lines = lines.lower()
lines = lines.replace(',', '').replace('.', '')
tokens = lines.split()
tokens = [token for token in tokens if len(token) > 7]
tokens.sort()
print(tokens)
