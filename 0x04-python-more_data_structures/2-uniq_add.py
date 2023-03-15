def uniq_add(my_list=[]):
    """
    Compute the sum of unique elements in a list.

    Args:
    my_list (list): A list of integers

    Returns:
    int: The sum of unique elements in the list.
    """
    # initialize the sum to zero
    result = 0
    for x in set(my_list):
        result += x
    return (result)
