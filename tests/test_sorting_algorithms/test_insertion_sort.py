from .scenario import SCENARIO
from sorting_algorithms import insertion_sort


def test_insertion_sort():
    for case, answer in SCENARIO:
        assert insertion_sort(case) == answer
