from typing import Union, List


def maximum(array: List[Union[int, float]]) -> Union[int, float]:
    """
    Find max value in input array.
    :param array: Input array.
    :return: Max value.
    """
    if not array:
        raise ValueError('Input array is empty')
    max_value = None
    for value in array:
        if max_value is None or value > max_value:
            max_value = value

    return max_value
