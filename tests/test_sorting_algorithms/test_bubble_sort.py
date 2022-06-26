from .scenario import SCENARIO
from sorting_algorithms import bubble_sort


def test_bubble_sort():
    for case, answer in SCENARIO:
        assert bubble_sort(case) == answer
