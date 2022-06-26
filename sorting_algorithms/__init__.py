from typing import Union

"""
Valid values of array elements for sorting.
"""
VALID_VALUES = Union[int, float, str]

from .utils import copy_array
from .bubble_sort import bubble_sort
from .insertion_sort import insertion_sort
from .selection_sort import selection_sort
