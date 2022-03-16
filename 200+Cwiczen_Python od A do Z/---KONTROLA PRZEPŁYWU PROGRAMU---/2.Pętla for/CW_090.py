# %%
text = 'Python jest bardzo popularnym językiem programowania'
result = []
idx = 0
for word in text.split(' '):
    if idx < 4:
        result.append(word.lower())
        idx += 1

print(result)

# -----------------------------------------------------------------------
text = 'Python jest bardzo popularnym językiem programowania'
words = text.split(' ')
result = []
for idx, word in enumerate(words):
    if idx < 4:
        result.append(word.lower())
print(result)

# ------------------------------------------------------------------------
text = 'Python jest bardzo popularnym językiem programowania'
words = text.split(' ')
result = [word.lower() for idx, word in enumerate(words) if idx < 4]
print(result)

# %%
