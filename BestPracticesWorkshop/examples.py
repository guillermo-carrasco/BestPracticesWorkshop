def sum_list(l):
    """Sum all elements in list

    :param l: List containing elements to sum
    :return: The sum of all elements in the list
    :rtype: int
    :raises ValueError: If there is any non-integer element on the list
    """
    if not all([isinstance(elem, int) for elem in l]):
        raise ValueError("All elements on the list must be integers!")
    return sum(l)

def odd(n):
    """Return the closest odd number to n

    :param n: An integer
    :return: The same integer if it is odd. The next integer otherwise
    :rtype: int
    :raises ValueError: If the parameter is not inteer
    """
    if not isinstance(n, int):
        raise ValueError("The parameter must be an integer!")
    if not n%2:
        return n+1
    return n
