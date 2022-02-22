
def add(x, y):
    """Zwraca sume dwóch liczb

    >>> add(3,4)
    7

    >>> add(2,8)
    100
    """

    return x+y


if __name__ == '__main__':
    import doctest
    # doctest.testmod()
    doctest.testfile('test.txt')
