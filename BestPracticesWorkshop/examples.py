def sum_list(lst):
    """Sum all elements in list

    :param lst: List containing elements to sum
    :return: The sum of all elements in the list
    :rtype: int
    :raises ValueError: If there is any non-integer element on the list
    """
    if not all([isinstance(elem, int) for elem in lst]):
        raise ValueError("All elements on the list must be integers!")
    return sum(lst)

def odd(num):
    """Return the closest odd number to n

    :param num: An integer
    :return: The same integer if it is odd. The next integer otherwise
    :rtype: int
    :raises ValueError: If the parameter is not inteer
    """
    if not isinstance(num, int):
        raise ValueError("The parameter must be an integer!")
    if not num%2:
        return num+1
    return num
