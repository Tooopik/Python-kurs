text = 'Programowanie w języku Python'

text_std = list(set((text.lower()).replace('ę', 'e')))
text_std.remove(' ')
text_std.sort()

print(text_std[:10])

# -----------------------------------------------------------------
text = 'Programowanie w języku Python'
text = text.lower()
text = text.replace('ę', 'e')
characters = list(set(text))
characters.remove(' ')
characters.sort()
print(characters[:10])
