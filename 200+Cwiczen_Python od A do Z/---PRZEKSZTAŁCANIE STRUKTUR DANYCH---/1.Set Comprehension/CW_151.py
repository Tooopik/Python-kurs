# %%
desc = "Playway: Playway to producent gier komputerowych."
print(len({word.replace(':', '').replace('.', '').lower()
      for word in desc.split()}))
# ---------------------------------------------------------------------
# %%
desc = "Playway: Playway to producent gier komputerowych."
word_list = desc.lower().replace(':', '').replace('.', '').split()
word_unique = {word for word in word_list}
print(len(word_unique))
