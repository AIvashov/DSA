from typing import Union, List


def median(array: List[Union[int, float]]) -> Union[int, float]:
    """
    Find median value in input array.
    :param array: Input array.
    :return: Median value.
    """
    if not array:
        raise ValueError('Input array is empty')

    array = sorted(array)
    len_array = len(array)
    middle = len_array // 2

    if len_array % 2 == 0:
        return (array[middle] + array[middle - 1]) / 2
    return array[middle]
