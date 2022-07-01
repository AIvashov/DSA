from .scenario import SCENARIO

from utils import copy_array
from sorting_algorithms import merge_sort


def test_merge_sort():
    for case, answer in SCENARIO:
        copy_case = copy_array(case)
        merge_sort(copy_case)
        assert copy_case == answer
