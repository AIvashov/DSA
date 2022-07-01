from stats import maximum, minimum, median
import statistics


def test_maximum():
    cases = [list(range(10)), list(range(19)), list(range(-10, 0)), [1, 1], [-1.5, 0, 3, -2, 3, 5, 5.0]]
    for case in cases:
        assert maximum(case) == max(case)


def test_minimum():
    cases = [list(range(10)), list(range(19)), list(range(-10, 0)), [1, 1], [-1.5, 0, 3, -2, 3, 5, 5.0]]
    for case in cases:
        assert minimum(case) == min(case)


def test_median():
    cases = [list(range(10)), list(range(19)), list(range(-10, 0)), [1, 1], [-1.5, 0, 3, -2, 3, 5, 5.0]]
    for case in cases:
        assert median(case) == statistics.median(case)
