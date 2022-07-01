from tests.test_sorting_algorithms.scenario import SCENARIO
from utils import copy_array


def test_copy_array():
    for case, answer in SCENARIO:
        assert id(copy_array(case)) != id(case)
        assert id(copy_array(answer)) != id(answer)

