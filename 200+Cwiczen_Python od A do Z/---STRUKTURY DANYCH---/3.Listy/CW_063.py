hashtags = ['summer', 'time', 'vibes']
a= ''
for word in hashtags:
    a += '#'+word
print(a)

#-----------------------------------------------------
hashtags = ['summer', 'time', 'vibes']
print('#' + '#'.join(hashtags))

print('+'.join(hashtags))