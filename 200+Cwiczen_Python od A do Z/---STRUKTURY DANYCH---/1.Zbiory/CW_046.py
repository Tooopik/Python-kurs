text = 'Programming in python.'
vowels = {'a', 'e', 'i', 'o', 'u'}

text = text.lower()
text = text.replace(' ', '')
text = text.replace('.', '')
a = set(text)

print(f'Liczba elementów: {len(a - vowels)}')

# -------------------------------------------------------------------
text = 'Programming in python.'
text = text.lower()
text = text.replace(' ', '')
text = text.replace('.', '')
vowels = {'a', 'e', 'i', 'o', 'u'}
letters = set(text)
consonants = letters.difference(vowels)
print(f'Liczba elementów: {len(consonants)}')
