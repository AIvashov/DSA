from .scenario import SCENARIO

from utils import copy_array
from sorting_algorithms import selection_sort


def test_selection_sort():
    for case, answer in SCENARIO:
        copy_case = copy_array(case)
        selection_sort(copy_case)
        assert copy_case == answer

