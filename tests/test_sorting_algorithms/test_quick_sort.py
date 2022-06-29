from .scenario import SCENARIO
from sorting_algorithms import copy_array, quick_sort


def test_quick_sort():
    for case, answer in SCENARIO:
        copy_case = copy_array(case)
        quick_sort(copy_case)
        assert copy_case == answer
