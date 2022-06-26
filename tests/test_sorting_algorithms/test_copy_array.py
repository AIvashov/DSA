from .scenario import SCENARIO
from sorting_algorithms import copy_array


def test_copy_array():
    for case, answer in SCENARIO:
        assert id(copy_array(case)) != id(case)
        assert id(copy_array(answer)) != id(answer)

