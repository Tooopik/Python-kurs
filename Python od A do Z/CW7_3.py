hashtags = '#weekend#good#time#'
word = ''

for i in hashtags:
    if i not in '#':
        word += i

    else:
        if word:
            print(word)
            word = ''
