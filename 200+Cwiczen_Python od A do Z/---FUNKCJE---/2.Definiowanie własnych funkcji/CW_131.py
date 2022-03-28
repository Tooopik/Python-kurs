def count_str(list):
    result = 0
    for object in list:
        if isinstance(object, str) == True:
            result += 1
    return result
