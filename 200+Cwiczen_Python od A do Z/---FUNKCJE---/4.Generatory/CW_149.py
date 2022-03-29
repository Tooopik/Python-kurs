# %%
from ast import Return


def dayname(idx):
    days = ['pon', 'wt', 'śr', 'czw', 'pt', 'sb', 'nd']
    result = []
    for i in range(-1, 2):
        result.append(days[idx + i])
    return result


# ------------------------------------------------------------
def dayname(index):
    days = ['pon', 'wt', 'śr', 'czw', 'pt', 'sb', 'nd']
    yield days[index - 1]
    yield days[index]
    yield days[(index + 1) % 7]
