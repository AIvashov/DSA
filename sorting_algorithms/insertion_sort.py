def insertion_sort(array: list):
    """


    """

    for top in range(1, len(array)):
        k = top
        while k > 0 and array[k-1] > array[k]:
            array[k], array[k-1] = array[k-1], array[k]
            k -= 1
