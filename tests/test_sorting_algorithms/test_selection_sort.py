from .scenario import SCENARIO
from sorting_algorithms import copy_array, selection_sort


def test_selection_sort():
    for case, answer in SCENARIO:
        copy_case = copy_array(case)
        selection_sort(copy_case)
        assert copy_case == answer

