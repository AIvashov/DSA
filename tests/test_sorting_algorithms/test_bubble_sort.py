from .scenario import SCENARIO
from sorting_algorithms import bubble_sort, copy_array


def test_bubble_sort():
    for case, answer in SCENARIO:
        copy_case = copy_array(case)
        bubble_sort(copy_case)
        assert copy_case == answer
