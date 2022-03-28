def is_distinct(a):
    if len(set(a)) == len(a):
        return True
    else:
        return False

# --------------------------------------


def is_distinct(items):
    return len(items) == len(set(items))
