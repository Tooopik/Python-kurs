def flatten(list):
    result = []
    [[result.append(item) for item in record] for record in list]
    return result


items = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(flatten(items))
# ---------------------------------------------------------------------------


def flatten2(items):
    result = []
    for item in items:
        result.extend(item)
    return result


print(flatten2(items))
