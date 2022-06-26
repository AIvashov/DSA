from .scenario import SCENARIO
from sorting_algorithms import selection_sort


def test_selection_sort():
    for case, answer in SCENARIO:
        assert selection_sort(case) == answer
