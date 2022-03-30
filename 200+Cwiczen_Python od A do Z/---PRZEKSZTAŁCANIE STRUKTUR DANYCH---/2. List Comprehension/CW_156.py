# %%
with open('gaming.txt', 'r', encoding='UTF-8') as file:
    text = file.readlines()
a = [word.replace('\n', '') for word in text]
b = [word for word in a if word != '']
print(b)

# %%
