# %%
text = 'Witaj na kursie Pythona.\nPython jest wspaniały!'
print(text)

# %%
dir(text)
# %%
help(str.count)
# %%
text.capitalize()
# %%
text.title()

# %%
text.count('Python')
# %%
text.startswith('Wi')
# %%
text.startswith('kurs')

# %%
text.endswith('ły!')

# %%
'sample.py'.endswith('.py')

# %%
text.find('Python')
# %%
text[text.find('Python'):]
# %%
hashtags = 'sport#gym'
idx = hashtags.find('#')
hashtags[:idx]

# %%
print('pawel'.isalnum())
print('pawel1234'.isalnum())
print('pawel 1'.isalnum())
print('pawel!'.isalnum())

# %%
'4536'.isdigit()
# %%
'python'.islower()
# %%
'python'.isupper()

# %%
' '.join(['python', '3.7'])
print('#'.join(['sport', 'gym', 'fit']))
# %%
'#good#time#mood'.replace('#', ' ')

# %%
'column name'.replace(' ', '_')

# %%
'        python      '.strip()

# %%
'        python      '.rstrip()
# %%
'        python      '.lstrip()
# %%
'1,2,3,4,5,6,7'.split(',')

# %%
'python java php sql sas'.split()

# %%
'#gym#fit#sport'.split('#')

# %%
'12'.zfill(5)

# %%
'1'.zfill(10)

# %%
