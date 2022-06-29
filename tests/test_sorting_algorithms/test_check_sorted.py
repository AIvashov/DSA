from .scenario import SCENARIO
from sorting_algorithms import check_sorted


def test_check_sorted():
    for case, answer in SCENARIO:
        assert not check_sorted(case)
        assert check_sorted(answer)
        assert check_sorted(answer[::-1], False)
