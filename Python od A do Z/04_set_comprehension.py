# %%
text = 'Python jest wspaniały. Python jest elastyczny. Python rządzi.'

# %%
words = text.lower().replace('.', '').split()

# %%
unique_words = {word for word in words}

# %%
unique_words_gt_4 = {word for word in words if len(word) > 4}

# %%
{word.capitalize() if word.startswith('pyt') else word for word in words}

# %%
