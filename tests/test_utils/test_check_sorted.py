from tests.test_sorting_algorithms.scenario import SCENARIO
from utils import check_sorted


def test_check_sorted():
    for case, answer in SCENARIO:
        assert not check_sorted(case)
        assert check_sorted(answer)
        assert check_sorted(answer[::-1], False)
