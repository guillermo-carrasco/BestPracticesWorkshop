def sum_list(l):
    """Sum all elements in list

    Params:
        l -- list to sum
    """
    if not all([isinstance(elem, int) for elem in l]):
        raise ValueError("All elements on the list must be integers!")
    return sum(l)

def odd(n):
    """Return the closest odd number to n

    Paramss:
        n - An integer
    """
    if not isinstance(n, int):
        raise ValueError("The parametermust be an integer!")
    if not n%2:
        return n+1
    return n
