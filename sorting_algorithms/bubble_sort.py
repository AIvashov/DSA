def bubble_sort(array: list):
    for bypass in range(1, len(array)):
        for k in range(0, len(array) - bypass):
            if array[k] > array[k+1]:
                array[k], array[k+1] = array[k+1], array[k]
