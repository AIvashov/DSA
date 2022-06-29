from .scenario import SCENARIO
from sorting_algorithms import insertion_sort, copy_array


def test_insertion_sort():
    for case, answer in SCENARIO:
        copy_case = copy_array(case)
        insertion_sort(copy_case)
        assert copy_case == answer

