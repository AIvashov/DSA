from typing import Union, List


def minimum(array: List[Union[int, float]]) -> Union[int, float]:
    """
    Find min value in input array.
    :param array: Input array.
    :return: Min value.
    """
    if not array:
        raise ValueError('Input array is empty')
    min_value = None
    for value in array:
        if min_value is None or value < min_value:
            min_value = value

    return min_value
