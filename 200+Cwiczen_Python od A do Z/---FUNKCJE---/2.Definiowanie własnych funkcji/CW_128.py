# %%
def map_longest(words):
    longestWord = 0
    for word in words:
        if len(word) > longestWord:
            longestWord = len(word)
    if longestWord > 0:
        return longestWord


print(map_longest(['python3', 'java', 'r']))
# ----------------------------------------------------------------
# %%


def map_longest(words):
    length = []
    for word in words:
        length.append(len(word))
    return max(length)
