from .scenario import SCENARIO

from utils import copy_array
from sorting_algorithms import insertion_sort


def test_insertion_sort():
    for case, answer in SCENARIO:
        copy_case = copy_array(case)
        insertion_sort(copy_case)
        assert copy_case == answer

