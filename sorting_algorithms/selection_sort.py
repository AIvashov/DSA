def selection_sort(array: list):
    """


    """
    for pos in range(0, len(array) - 1):
        for k in range(pos+1, len(array)):
            if array[k] < array[pos]:
                array[k], array[pos] = array[pos], array[k]
